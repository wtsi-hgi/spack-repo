from spack.package import *
from spack.util.executable import Executable


class Germline2(MakefilePackage):
    """Efficiently identify shared genetic segments (IBD) in large cohorts."""

    homepage = "https://github.com/gusevlab/germline2"
    url = "https://github.com/gusevlab/germline2/archive/refs/tags/v1.0.tar.gz"

    license("MIT")

    version("1.0", sha256="0b4e0c9a6fac211f605c5e6de7f2b4e0a34c1dd68e9238514bb6fd125504275a")

    depends_on("boost@1.57.0:")

    def build(self, spec, prefix):
        make(
            "INCL=-I{0}".format(spec["boost"].prefix.include),
            "CXX={0}".format(self.compiler.cxx),
        )
        cxx = Executable(self.compiler.cxx)
        cxx("-O3", "-std=c++11", "parse_bmatch.cpp", "-o", "parse_bmatch")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("g2", prefix.bin)
        install("parse_bmatch", prefix.bin)

        datadir = join_path(prefix.share, "germline2")
        mkdirp(datadir)
        install("README.md", datadir)
        install("LICENSE", datadir)
        install_tree("example", join_path(datadir, "example"))

    @run_after("install")
    def install_test(self):
        """Run the bundled example to verify the binary."""
        data_dir = join_path(self.prefix.share, "germline2", "example")
        g2 = Executable(join_path(self.prefix.bin, "g2"))
        with working_dir("spack-test", create=True):
            g2(
                "-m",
                "0.9",
                join_path(data_dir, "SIM.NE_20000.MATCH_FREQ.SHAPEIT.haps"),
                join_path(data_dir, "SIM.NE_20000.MATCH_FREQ.SHAPEIT.sample"),
                join_path(data_dir, "genMap.1KG.b37.chr1.map"),
                "germline2-example.match",
            )
