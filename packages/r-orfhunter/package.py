# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrfhunter(RPackage):
    """Predict open reading frames in nucleotide sequences

    The ORFhunteR package is a R and C++ library for an automatic determination and annotation of open reading frames (ORF) in a large set of RNA molecules. It efficiently implements the machine learning model based on vectorization of nucleotide sequences and the random forest classification algorithm. The ORFhunteR package consists of a set of functions written in the R language in conjunction with C++. The efficiency of the package was confirmed by the examples of the analysis of RNA molecules from the NCBI RefSeq and Ensembl databases. The package can be used in basic and applied biomedical research related to the study of the transcriptome of normal as well as altered (for example, cancer) human cells.
    """

    bioc = "ORFhunteR"

    version("1.16.0", commit="926799f1653d3ea3aeb1b5157c9f96ea533d97f1")
    version("1.10.0", commit="76c58ae13c2067fa9b6fabaea664f09ffdf6b04b")

    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-peptides", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg38", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-randomforest", type=("build", "run"))
    depends_on("r-xfun", type=("build", "run"))
