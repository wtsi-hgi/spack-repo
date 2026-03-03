from spack.package import *


class GithubCli(MakefilePackage):
    """GitHub CLI brings GitHub to your terminal. It helps you do
    everyday GitHub tasks without ever leaving the terminal.

    This package builds from source using the project's Makefile and
    installs the `gh` binary, manpages, and shell completions.
    """

    homepage = "https://github.com/cli/cli"
    url = "https://github.com/cli/cli/archive/refs/tags/v2.40.0.tar.gz"

    maintainers("wtsi-hgi")

    # Choose a version compatible with Go available in Spack
    version("2.40.0", sha256="7c3ebebd285980e96718d2a39f902a538270c162e5be3e49f2f285fb9dc97bdf")

    # Build dependencies
    depends_on("go@1.21:", type="build")
    depends_on("git", type=("build", "run"))

    # The upstream Makefile honors `prefix`/`bindir`/`datadir`/`mandir` variables
    # and generates manpages + shell completions.
    def build(self, spec, prefix):
        make("bin/gh")

    def install(self, spec, prefix):
        make("install", f"prefix={prefix}")

    @run_after("install")
    def install_test(self):
        # CLI presence / basic sanity
        with working_dir("spack-test", create=True):
            gh = Executable(join_path(self.prefix.bin, "gh"))
            gh("--version")

