# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesubs(RPackage):
    """DEsubs: an R package for flexible identification of differentially expressed subpathways using RNA-seq expression experiments

    DEsubs is a network-based systems biology package that extracts disease-perturbed subpathways within a pathway network as recorded by RNA-seq experiments. It contains an extensive and customizable framework covering a broad range of operation modes at all stages of the subpathway analysis, enabling a case-specific approach. The operation modes refer to the pathway network construction and processing, the subpathway extraction, visualization and enrichment analysis with regard to various biological and pharmacological features. Its capabilities render it a tool-guide for both the modeler and experimentalist for the identification of more robust systems-level biomarkers for complex diseases.
    """

    bioc = "DEsubs"

    version("1.34.0", commit="52e13e1773f2c4c0a876b5d276adc96b1977031e")
    version("1.28.0", commit="a59b0e4cd8b139fa79906867d25083da592d3044")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-locfit", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-rbgl", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-ebseq", type=("build", "run"))
    depends_on("r-nbpseq", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
