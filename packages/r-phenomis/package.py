# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenomis(RPackage):
	"""Postprocessing and univariate analysis of omics data

	The 'phenomis' package provides methods to perform post-processing (i.e. quality control and normalization) as well as univariate statistical analysis of single and multi-omics data sets. These methods include quality control metrics, signal drift and batch effect correction, intensity transformation, univariate hypothesis testing, but also clustering (as well as annotation of metabolomics data). The data are handled in the standard Bioconductor formats (i.e. SummarizedExperiment and MultiAssayExperiment for single and multi-omics datasets, respectively; the alternative ExpressionSet and MultiDataSet formats are also supported for convenience). As a result, all methods can be readily chained as workflows. The pipeline can be further enriched by multivariate analysis and feature selection, by using the 'ropls' and 'biosigner' packages, which support the same formats. Data can be conveniently imported from and exported to text files. Although the methods were initially targeted to metabolomics data, most of the methods can be applied to other types of omics data (e.g., transcriptomics, proteomics).
	"""
	
	homepage = "https://doi.org/10.1038/s41597-021-01095-3"
	bioc = "phenomis" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/phenomis_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/phenomis/phenomis_1.4.0.tar.gz"]

    version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="2f002955d854868a2fd87bcea8902662a4f7089f07d83b490403d00034e1d9fd")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biodb", type=("build", "run"))
	depends_on("r-biodbchebi", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-multidataset", type=("build", "run"))
	depends_on("r-pmcmrplus", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ropls", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
