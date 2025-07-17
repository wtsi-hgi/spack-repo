# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTronco(RPackage):
    """TRONCO, an R package for TRanslational ONCOlogy

    The TRONCO (TRanslational ONCOlogy) R package collects algorithms to infer progression models via the approach of Suppes-Bayes Causal Network, both from an ensemble of tumors (cross-sectional samples) and within an individual patient (multi-region or single-cell samples). The package provides parallel implementation of algorithms that process binary matrices where each row represents a tumor sample and each column a single-nucleotide or a structural variant driving the progression; a 0/1 value models the absence/presence of that alteration in the sample. The tool can import data from plain, MAF or GISTIC format files, and can fetch it from the cBioPortal for cancer genomics. Functions for data manipulation and visualization are provided, as well as functions to import/export such data to other bioinformatics tools for, e.g, clustering or detection of mutually exclusive alterations. Inferred models can be visualized and tested for their confidence via bootstrap and cross-validation. TRONCO is used for the implementation of the Pipeline for Cancer Inference (PICNIC).
    """

    homepage = "https://sites.google.com/site/troncopackage/"
    bioc = "TRONCO"

    version("2.40.0", commit="543c8798c87d491a3c726ad9042900059a4b2dc5")
    version("2.34.0", commit="74dffd8ba864fa55759395d4932330853dde6ac4")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-bnlearn", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-iterators", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-xtable", type=("build", "run"))
    depends_on("r-gtable", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-r-matlab", type=("build", "run"))
