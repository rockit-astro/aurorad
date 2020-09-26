RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

GIT_VERSION = $(shell git name-rev --name-only --tags --no-undefined HEAD 2>/dev/null || echo git-`git rev-parse --short HEAD`)
SERVER_VERSION=$(shell awk '/Version:/ { print $$2; }' onemetre-vaisala-server.spec)

all:
	mkdir -p build
	cp aurorad aurorad.bak
	awk '{sub("SOFTWARE_VERSION = .*$$","SOFTWARE_VERSION = \"$(SERVER_VERSION) ($(GIT_VERSION))\""); print $0}' aurorad.bak > aurorad
	${RPMBUILD} -ba observatory-aurora-server.spec
	${RPMBUILD} -ba observatory-aurora-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-aurora.spec

	mv build/noarch/*.rpm .
	rm -rf build
	mv aurorad.bak aurorad
