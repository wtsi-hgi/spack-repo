# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ngsrelate(MakefilePackage):
    """NgsRelate infers relatedness and inbreeding coefficients from low-coverage
    next-generation sequencing data by operating directly on genotype likelihoods.
    """

    homepage = "https://github.com/ANGSD/NgsRelate"
    url = "https://github.com/ANGSD/NgsRelate/archive/refs/tags/v2.0.tar.gz"
    git = "https://github.com/ANGSD/NgsRelate.git"

    license("GPL-2.0-only")

    version("2.0", sha256="f2c20228720298d6ef2fd34324449ba7ebdd4b987477c78bd20ed99f176218c6")

    def url_for_version(self, version):
        return f"https://github.com/ANGSD/NgsRelate/archive/refs/tags/v{version}.tar.gz"

    depends_on("htslib", type=("build", "link", "run"))
    depends_on("curl", type=("build", "link", "run"))
    depends_on("zlib", type=("build", "link", "run"))
    depends_on("bzip2", type=("build", "link", "run"))
    depends_on("xz", type=("build", "link", "run"))

    def patch(self):
        """Respect externally provided linker flags for htslib."""
        filter_file(
            "$(CXX) $(FLAGS)  -o ngsRelate",
            "$(CXX) $(FLAGS) $(LDFLAGS) -o ngsRelate",
            "Makefile",
            string=True,
        )

    def setup_build_environment(self, env):
        spec = self.spec

        hts_headers = spec["htslib"].headers
        if hts_headers:
            env.append_flags("CXXFLAGS", hts_headers.include_flags)

        hts_libs = spec["htslib"].libs
        if hts_libs:
            env.append_flags("LDFLAGS", hts_libs.ld_flags)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("ngsRelate", prefix.bin)

    @run_after("install")
    def install_test(self):
        """Invoke the binary to ensure it was linked and is runnable."""
        ngsrelate = Executable(join_path(self.prefix.bin, "ngsRelate"))
        with working_dir("spack-test", create=True):
            ngsrelate()
