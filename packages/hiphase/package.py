from spack.package import *


class Hiphase(Package):
    """HiPhase is a tool for jointly phasing small, structural, and tandem
    repeat variants for PacBio sequencing data."""

    homepage = "https://github.com/PacificBiosciences/HiPhase"
    url = "https://github.com/PacificBiosciences/HiPhase/releases/download/v1.7.0/hiphase-v1.7.0-x86_64-unknown-linux-gnu.tar.gz"

    maintainers("twestbrookunf")

    license("BSD-3-Clause")

    version("1.7.0", sha256="01bc4c0ef1fda876578a9cd01adddca55a9b1402b40a839690722011b5babfc5")

    depends_on("patchelf", type="build")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("hiphase", prefix.bin)
        install("hiphase.md5", prefix)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            hiphase = Executable(self.prefix.bin.hiphase)
            hiphase("--help")
