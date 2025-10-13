import os

from spack.package import *


class Rnaseqc(MakefilePackage):
    """RNA-SeQC 2: fast, accurate RNA-seq metrics and QC tool.

    Builds the native C++ implementation from source. Upstream vendors SeqLib
    as a git submodule; we fetch with submodules enabled to ensure sources are
    present.
    """

    homepage = "https://github.com/getzlab/rnaseqc"
    git = "https://github.com/getzlab/rnaseqc.git"

    # SeqLib autotools build is not parallel-safe
    parallel = False

    # Use full commit for reproducibility; include submodules for SeqLib/htslib
    version(
        "2.4.2",
        commit="21dbf60cc580a4ce9b5d0a8303ca2f04eb62aa47",
        submodules=True,
    )

    # Dependencies required by the Makefile link line
    depends_on("boost+filesystem+regex+system")
    depends_on("zlib")
    depends_on("xz")
    depends_on("bzip2")

    def patch(self):
        # Upstream Makefile hardcodes CC=g++ and uses it for C++ compilation,
        # which leaks CC=g++ into the SeqLib autotools build and breaks it.
        # Teach the Makefile to use CXX for C++ and set CC to a C compiler.
        filter_file(r"^CC=g\+\+", "CXX?=g++\nCC?=gcc", "Makefile", string=True)
        filter_file(r"\$\(CC\)", "$(CXX)", "Makefile", string=True)
        # Ensure -fcommon to avoid multiple definition failures in bundled BWA
        filter_file("CFLAGS=", "CFLAGS= -fcommon ", "Makefile", string=True)
        # Also ensure bundled BWA builds with -fcommon
        for rel in ("SeqLib/bwa/Makefile", "SeqLib/bwa/Makefile.in"):
            if os.path.exists(rel):
                filter_file("CFLAGS=", "CFLAGS= -fcommon ", rel, string=True)
        for rel in ("SeqLib/fermi-lite/Makefile", "SeqLib/fermi-lite/Makefile.in"):
            if os.path.exists(rel):
                filter_file("CFLAGS=", "CFLAGS= -fcommon ", rel, string=True)

    # Build via upstream Makefile; default target is 'rnaseqc'
    def build(self, spec, prefix):
        include_flags = [
            "-ISeqLib",
            "-ISeqLib/htslib",
            f"-I{spec['boost'].headers.directories[0]}",
            f"-I{spec['zlib'].headers.directories[0]}",
            f"-I{spec['xz'].headers.directories[0]}",
            f"-I{spec['bzip2'].headers.directories[0]}",
        ]
        library_paths = [
            f"-L{spec['boost'].libs.directories[0]}",
            f"-L{spec['zlib'].libs.directories[0]}",
            f"-L{spec['xz'].libs.directories[0]}",
            f"-L{spec['bzip2'].libs.directories[0]}",
        ]

        # Do not override CC to avoid breaking SeqLib's autotools build; rely
        # on Spack's compiler wrappers picked up via PATH.
        make(
            "rnaseqc",
            "INCLUDE_DIRS=" + " ".join(include_flags),
            "LIBRARY_PATHS=" + " ".join(library_paths),
        )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("rnaseqc", prefix.bin)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # Prefer command-line test over heavy data-dependent tests.
            exe = join_path(self.prefix.bin, "rnaseqc")
            self.run_test(exe, options=["--version"], purpose="check rnaseqc runs")
