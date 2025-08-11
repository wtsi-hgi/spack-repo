# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamr(RPackage):
    """Detection of Rare Aberrantly Methylated Regions in Array and NGS Data

    ramr is an R package for detection of low-frequency aberrant methylation events in large data sets obtained by methylation profiling using array or high-throughput bisulfite sequencing. In addition, package provides functions to visualize found aberrantly methylated regions (AMRs), to generate sets of all possible regions to be used as reference sets for enrichment analysis, and to generate biologically relevant test data sets for performance evaluation of AMR/DMR search algorithms.
    """

    homepage = "https://github.com/BBCG/ramr"
    bioc = "ramr"

    version("1.16.0", commit="a19305bc3061062ece0985747cb04d87001ff433")
    version("1.10.0", commit="4a632c193c27d7ec9b206cc2eb34fbde9bf3e6b9")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-dorng", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-envstats", type=("build", "run"))
    depends_on("r-extdist", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))

    def patch(self):
        # Ensure we link against Rcpp shared library. Upstream Makevars overrides PKG_LIBS
        # and omits Rcpp's linker flags, which leads to undefined symbols at load time.
        # Replace literal assignment to include Rcpp LdFlags
        # Rcpp:::LdFlags() can be NULL on newer Rcpp, so compute explicit flags
        # that link against and runtime-load the Rcpp shared library.
        # We query the Rcpp libs directory from R and add -L, -l and rpath.
        filter_file(
            "PKG_LIBS = $(SHLIB_OPENMP_CXXFLAGS)",
            "PKG_LIBS = $(SHLIB_OPENMP_CXXFLAGS) $(shell \"$(R_HOME)\"/bin/Rscript -e 'lib<-system.file(\"libs\", package=\"Rcpp\"); if (nzchar(lib)) cat(paste0(\"-Wl,-rpath,\",lib,\" \", file.path(lib, \"Rcpp.so\")))')",
            "src/Makevars",
            string=True,
        )

        # Workaround for missing instantiation of Rcpp::standard_delete_finalizer<std::vector<double>>
        # Force the template to be instantiated in this package's shared library.
        inst_src = join_path(self.stage.source_path, "src", "rcpp_instantiations.cpp")
        with open(inst_src, "w") as f:
            f.write(
                "#include <Rcpp.h>\n"
                "#include <vector>\n"
                "template void Rcpp::standard_delete_finalizer<std::vector<double>>(std::vector<double>*);\n"
                "template void Rcpp::standard_delete_finalizer<std::vector<unsigned int>>(std::vector<unsigned int>*);\n"
            )

    def setup_build_environment(self, env):
        # Ensure the Rcpp shared library is discoverable at link and run time
        rcpp_prefix = self.spec["r-rcpp"].prefix
        rcpp_libs_dir = join_path(rcpp_prefix, "rlib", "R", "library", "Rcpp", "libs")
        # Add rpath and -L/-l for Rcpp as an extra safeguard
        env.append_flags("LDFLAGS", f"-Wl,-rpath,{rcpp_libs_dir} -L{rcpp_libs_dir} -lRcpp")
