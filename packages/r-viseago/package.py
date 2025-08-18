# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViseago(RPackage):
    """ViSEAGO: a Bioconductor package for clustering biological functions using Gene Ontology and semantic similarity

    The main objective of ViSEAGO package is to carry out a data mining of biological functions and establish links between genes involved in the study. We developed ViSEAGO in R to facilitate functional Gene Ontology (GO) analysis of complex experimental design with multiple comparisons of interest. It allows to study large-scale datasets together and visualize GO profiles to capture biological knowledge. The acronym stands for three major concepts of the analysis: Visualization, Semantic similarity and Enrichment Analysis of Gene Ontology. It provides access to the last current GO annotations, which are retrieved from one of NCBI EntrezGene, Ensembl or Uniprot databases for several species. Using available R packages and novel developments, ViSEAGO extends classical functional GO analysis to focus on functional coherence by aggregating closely related biological themes while studying multiple datasets at once. It provides both a synthetic and detailed view using interactive functionalities respecting the GO graph structure and ensuring functional coherence supplied by semantic similarity. ViSEAGO has been successfully applied on several datasets from different species with a variety of biological questions. Results can be easily shared between bioinformaticians and biologists, enhancing reporting capabilities while maintaining reproducibility.
    """

    homepage = "https://www.bioconductor.org/packages/release/bioc/html/ViSEAGO.html"
    bioc = "ViSEAGO"

    version("1.22.0", commit="7d2965b8251c44be9bc21933eaa654ecb0662369")
    version("1.16.0", commit="21e6693b42d99aa321d9ebd068e0b30288c7933b")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-annotationforge", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-dendextend", type=("build", "run"))
    depends_on("r-diagrammer", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-dynamictreecut", type=("build", "run"))
    depends_on("r-fgsea", type=("build", "run"))
    depends_on("r-gosemsim", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-heatmaply", type=("build", "run"))
    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    # Required for heatmap visualizations used by ViSEAGO
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-processx", type=("build", "run"))
    depends_on("r-topgo", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-upsetr", type=("build", "run"))
