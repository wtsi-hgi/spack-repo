# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMageckflute(RPackage):
    """Integrative Analysis Pipeline for Pooled CRISPR Functional Genetic Screens

    CRISPR (clustered regularly interspaced short palindrome repeats) coupled with nuclease Cas9 (CRISPR/Cas9) screens represent a promising technology to systematically evaluate gene functions. Data analysis for CRISPR/Cas9 screens is a critical process that includes identifying screen hits and exploring biological functions for these hits in downstream analysis. We have previously developed two algorithms, MAGeCK and MAGeCK-VISPR, to analyze CRISPR/Cas9 screen data in various scenarios. These two algorithms allow users to perform quality control, read count generation and normalization, and calculate beta score to evaluate gene selection performance. In downstream analysis, the biological functional analysis is required for understanding biological functions of these identified genes with different screening purposes. Here, We developed MAGeCKFlute for supporting downstream analysis. MAGeCKFlute provides several strategies to remove potential biases within sgRNA-level read counts and gene-level beta scores. The downstream analysis with the package includes identifying essential, non-essential, and target-associated genes, and performing biological functional category analysis, pathway enrichment analysis and protein complex enrichment analysis of these genes. The package also visualizes genes in multiple ways to benefit users exploring screening data. Collectively, MAGeCKFlute enables accurate identification of essential, non-essential, and targeted genes, as well as their related biological functions. This vignette explains the use of the package and demonstrates typical workflows.
    """

    bioc = "MAGeCKFlute"

    version("2.12.0", commit="40772ead1ef9c7fddddd19dbd9893bca8551c03d")
    version("2.6.0", commit="af17351d93c2975507e60c9827e8a4ca7efc428a")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-dose", type=("build", "run"))
    depends_on("r-clusterprofiler", type=("build", "run"))
    depends_on("r-pathview", type=("build", "run"))
    depends_on("r-enrichplot", type=("build", "run"))
    depends_on("r-msigdbr", type=("build", "run"))
    depends_on("r-depmap", type=("build", "run"))
