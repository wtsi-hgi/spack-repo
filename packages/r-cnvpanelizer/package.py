# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvpanelizer(RPackage):
    """Reliable CNV detection in targeted sequencing applications

    A method that allows for the use of a collection of non-matched normal tissue samples. Our approach uses a non-parametric bootstrap subsampling of the available reference samples to estimate the distribution of read counts from targeted sequencing. As inspired by random forest, this is combined with a procedure that subsamples the amplicons associated with each of the targeted genes. The obtained information allows us to reliably classify the copy number aberrations on the gene level.
    """

    bioc = "CNVPanelizer"

    version("1.40.0", commit="48b552ebebb4ab28253c341f22ae363bee5c82bf")
    version("1.34.0", commit="ca119f65085113614fb6c1d82c8d6f51a365037a")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-noiseq", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-exomecopy", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinyfiles", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-openxlsx", type=("build", "run"))
