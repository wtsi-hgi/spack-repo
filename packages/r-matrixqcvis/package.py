# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixqcvis(RPackage):
    """Shiny-based interactive data-quality exploration for omics data

    Data quality assessment is an integral part of preparatory data analysis to ensure sound biological information retrieval. We present here the MatrixQCvis package, which provides shiny-based interactive visualization of data quality metrics at the per-sample and per-feature level. It is broadly applicable to quantitative omics data types that come in matrix-like format (features x samples). It enables the detection of low-quality samples, drifts, outliers and batch effects in data sets. Visualizations include amongst others bar- and violin plots of the (count/intensity) values, mean vs standard deviation plots, MA plots, empirical cumulative distribution function (ECDF) plots, visualizations of the distances between samples, and multiple types of dimension reduction plots. Furthermore, MatrixQCvis allows for differential expression analysis based on the limma (moderated t-tests) and proDA (Wald tests) packages. MatrixQCvis builds upon the popular Bioconductor SummarizedExperiment S4 class and enables thus the facile integration into existing workflows. The package is especially tailored towards metabolomics and proteomics mass spectrometry data, but also allows to assess the data quality of other data types that can be represented in a SummarizedExperiment object.
    """

    bioc = "MatrixQCvis"

    version("1.16.0", commit="0abd04184843495db6b4def5b5fce7fefccac3fb")
    version("1.10.0", commit="912411298ae15c05f88cb5e108388380dd145972")

    depends_on("r-summarizedexperiment@1.20:", type=("build", "run"))
    depends_on("r-plotly@4.9.3:", type=("build", "run"))
    depends_on("r-shiny@1.6:", type=("build", "run"))
    depends_on("r-complexheatmap@2.7.9:", type=("build", "run"))
    depends_on("r-dplyr@1.0.5:", type=("build", "run"))
    depends_on("r-experimenthub@2.6:", type=("build", "run"))
    depends_on("r-dt@0.33:", type=("build", "run"))
    depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
    depends_on("r-hmisc@4.5.0:", type=("build", "run"))
    depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
    depends_on("r-impute@1.65:", type=("build", "run"))
    depends_on("r-imputelcmd@2:", type=("build", "run"))
    depends_on("r-limma@3.47.12:", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-mass@7.3.58.1:", type=("build", "run"))
    depends_on("r-pcamethods@1.83:", type=("build", "run"))
    depends_on("r-proda@1.5:", type=("build", "run"))
    depends_on("r-rlang@0.4.10:", type=("build", "run"))
    depends_on("r-rmarkdown@2.7:", type=("build", "run"))
    depends_on("r-rtsne@0.15:", type=("build", "run"))
    depends_on("r-shinydashboard@0.7.1:", type=("build", "run"))
    depends_on("r-shinyhelper@0.3.2:", type=("build", "run"))
    depends_on("r-shinyjs@2:", type=("build", "run"))
    depends_on("r-tibble@3.1.1:", type=("build", "run"))
    depends_on("r-tidyr@1.1.3:", type=("build", "run"))
    depends_on("r-umap@0.2.7:", type=("build", "run"))
    depends_on("r-upsetr@1.4:", type=("build", "run"))
    depends_on("r-vsn@3.59.1:", type=("build", "run"))
