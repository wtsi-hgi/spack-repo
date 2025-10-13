from spack.package import *


class RnaSeqc2(Package):
    """
    RNA-SeQC computes a series of quality control metrics for RNA-Seq data.
    This package installs the prebuilt static Linux binary for v2.4.2.
    """

    homepage = "https://github.com/getzlab/rnaseqc"
    url = "https://github.com/getzlab/rnaseqc/releases/download/v2.4.2/rnaseqc.v2.4.2.linux.gz"

    maintainers = []

    version(
        "2.4.2",
        sha256="5505022cec1c99fcd9d36e3b3ca22ebd2d0f547658ce52e4fa90d82dd1430926",
        expand=False,
    )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)

        # Decompress the downloaded binary and place it as 'rnaseqc'
        archive = self.stage.archive_file
        dest_tmp = join_path(self.stage.path, "rnaseqc.v{0}.linux".format(self.version))
        gzip = which("gzip")
        with open(dest_tmp, "wb") as out:
            gzip("-dc", archive, output=out)

        dest = join_path(prefix.bin, "rnaseqc")
        install(dest_tmp, dest)
        set_executable(dest)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            rnaseqc = Executable(join_path(self.prefix.bin, "rnaseqc"))
            rnaseqc("--version")
