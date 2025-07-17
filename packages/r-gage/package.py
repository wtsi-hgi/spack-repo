# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGage(RPackage):
    """Generally Applicable Gene-set Enrichment for Pathway Analysis

    GAGE is a published method for gene set (enrichment or GSEA) or pathway analysis. GAGE is generally applicable independent of microarray or RNA-Seq data attributes including sample sizes, experimental designs, assay platforms, and other types of heterogeneity, and consistently achieves superior performance over other frequently used methods. In gage package, we provide functions for basic GAGE analysis, result processing and presentation. We have also built pipeline routines for of multiple GAGE analyses in a batch, comparison between parallel analyses, and combined analysis of heterogeneous data from different sources/studies. In addition, we provide demo microarray data and commonly used gene set data based on KEGG pathways and GO terms. These funtions and data are also useful for gene set analysis using other methods.
    """

    homepage = "https://github.com/datapplab/gage"
    bioc = "gage"

    version("2.58.0", commit="a5f163f25570e94e236636273bd388c4071c7dfc")
    version("2.52.0", commit="29b7ace8266822c309e518250d04e83cfedf53bc")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-keggrest", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
