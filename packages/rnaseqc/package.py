from spack.package import *


class Rnaseqc(MakefilePackage):
    """
    RNA-SeQC: RNA-seq metrics and QC tool from the Getz Lab.

    Builds the C++ v2 implementation which vendors SeqLib/htslib as a
    git submodule. Provides a single command-line executable: `rnaseqc`.
    """

    homepage = "https://github.com/getzlab/rnaseqc"
    git = "https://github.com/getzlab/rnaseqc.git"

    # Disable parallel make to avoid racing in SeqLib configure/build
    parallel = False

    # Use git with submodules to ensure SeqLib is present
    version("2.4.2", tag="v2.4.2", submodules=True)

    # Core dependencies used by SeqLib/htslib and rnaseqc
    depends_on("boost+regex+filesystem+system", type=("build", "link"))
    depends_on("zlib", type=("build", "link"))
    depends_on("bzip2", type=("build", "link"))
    depends_on("xz", type=("build", "link"))

    # Build-time tools for regenerating SeqLib autotools files and feature detection
    depends_on("pkgconfig", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    # Build targets
    build_targets = ["rnaseqc"]

    def patch(self):
        # Ensure SeqLib's autotools are regenerated with modern tools before configure
        # Upstream Makefile builds SeqLib via: `cd SeqLib && ./configure && make ... && make install`
        # Replace it to run `autoreconf -fi` first to avoid missing/old scripts issues
        filter_file(
            'cd SeqLib && ./configure && make CXXFLAGS="$(SEQFLAGS)" && make install',
            'cd SeqLib && autoreconf -fi && CPP="g++ -E" ./configure && make CXXFLAGS="$(SEQFLAGS) -fcommon" CFLAGS="-fcommon" && make install',
            'Makefile',
            string=True,
        )

    def build(self, spec, prefix):
        # Compose include and library paths for dependencies
        include_dirs = [
            "-ISeqLib",
            "-ISeqLib/htslib",
            f"-I{spec['boost'].headers.directories[0]}",
        ]

        library_paths = [
            f"-L{spec['boost'].libs.directories[0]}",
            f"-L{spec['zlib'].libs.directories[0]}",
            f"-L{spec['bzip2'].libs.directories[0]}",
            f"-L{spec['xz'].libs.directories[0]}",
        ]

        # Invoke make; the Makefile will build SeqLib/htslib first
        make(
            "rnaseqc",
            "INCLUDE_DIRS={0}".format(" ".join(include_dirs)),
            "LIBRARY_PATHS={0}".format(" ".join(library_paths)),
        )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("rnaseqc", prefix.bin)

    @run_after("install")
    def install_test(self):  # basic runtime test
        with working_dir("spack-test", create=True):
            rnaseqc = Executable(join_path(self.prefix.bin, "rnaseqc"))
            rnaseqc("--version")
