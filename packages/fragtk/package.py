from spack.package import *


class Fragtk(Package):
    """Fast and efficient toolkit implemented in Rust for working with fragment files."""

    maintainers("softpack-bot")

    homepage = "https://github.com/stuart-lab/fragtk"
    url = "https://github.com/stuart-lab/fragtk/archive/refs/tags/1.6.tar.gz"

    license("MIT")

    version("1.6", sha256="7dce1f0e8d04c730c4eb3d1ab51d9064396e0806088c07dd05ca72cf900ffcb9")

    depends_on("rust@1.85:", type="build")
    depends_on("cmake", type="build")

    def install(self, spec, prefix):
        cargo = Executable(join_path(spec["rust"].prefix.bin, "cargo"))
        cargo("install", "--locked", "--root", prefix, "--path", ".")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            fragtk = Executable(join_path(self.prefix.bin, "fragtk"))
            fragtk("--help")
