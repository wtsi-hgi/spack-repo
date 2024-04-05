# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RCellchat(RPackage):
    """CellChat is an R package designed for inference, analysis, and visualization of cell-cell communication from single-cell data. CellChat aims to enable users to identify and interpret cell-cell communication within an easily interpretable framework, with the emphasis of clear, attractive, and interpretable visualizations."""

    homepage = "https://github.com/sqjin/CellChat"
    url = "https://github.com/sqjin/CellChat/archive/refs/tags/v1.5.0.tar.gz"

	version("1.5.0", sha256="c9e31327cbbcf1fec5e6d8a0dfe011ded8e543557107e93dd4a417c4c137d1c6")
	version("1.0.0", sha256="f678ba2acaff891488e846cfee57619d2fecebd053af90e17042729ff58094b7")

    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-future", type=("build", "run"))
    depends_on("r-future-apply", type=("build", "run"))
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-nmf@0.23.0:", type=("build", "run"))
    depends_on("r-ggalluvial", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-svglite", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-expm", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-circlize@0.4.12:", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-rspectra", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-sna", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-fnn", type=("build", "run"))
    depends_on("r-shape", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))

    @run_before("install")
    def build_cpp(self):
        gcc = which("gcc")

        #gcc("src/RcppExports.cpp", "-I"+self.spec["r-rcppeigen"].prefix.rlib.R.library.RcppEigen.include, "-I"+self.spec["r-rcpp"].prefix.rlib.R.library.Rcpp.include, "-I"+self.spec["r"].prefix.rlib.R.include, "-o", "src/RcppExports.o")
        #gcc("src/CellChat_Rcpp.cpp", "-I"+self.spec["r-rcppeigen"].prefix.rlib.R.library.RcppEigen.include, "-I"+self.spec["r-rcpp"].prefix.rlib.R.library.Rcpp.include, "-I"+self.spec["r"].prefix.rlib.R.include, "-o", "src/CellChat_Rcpp.o")
        gcc("-shared", "-o" "src/CellChat.so", "-fPIC", "-I"+self.spec["r-rcppeigen"].prefix.rlib.R.library.RcppEigen.include, "-I"+self.spec["r-rcpp"].prefix.rlib.R.library.Rcpp.include, "-I"+self.spec["r"].prefix.rlib.R.include, "src/RcppExports.cpp", "src/CellChat_Rcpp.cpp")
