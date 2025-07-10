# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpiat(RPackage):
	"""Spatial Image Analysis of Tissues

	SPIAT (**Sp**atial **I**mage **A**nalysis of **T**issues) is an R package with a suite of data processing, quality control, visualization and data analysis tools. SPIAT is compatible with data generated from single-cell spatial proteomics platforms (e.g. OPAL, CODEX, MIBI, cellprofiler). SPIAT reads spatial data in the form of X and Y coordinates of cells, marker intensities and cell phenotypes. SPIAT includes six analysis modules that allow visualization, calculation of cell colocalization, categorization of the immune microenvironment relative to tumor areas, analysis of cellular neighborhoods, and the quantification of spatial heterogeneity, providing a comprehensive toolkit for spatial data analysis.
	"""
	
	homepage = "https://trigosteam.github.io/SPIAT/"
	bioc = "SPIAT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SPIAT_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SPIAT/SPIAT_1.4.2.tar.gz"]

	version("1.4.2", sha256="f23473c8b33b483e020b874cd1a8a1cc3149304d6b1cc7f15fdb0ae7bbdf3fbb")
	version("1.4.1", md5="45342ea9b5cbfbc01e38d6c7b7866852")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-spatialexperiment@1.8:", type=("build", "run"))
	depends_on("r-apcluster@1.4.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-gtools@3.8.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-rann@2.6.1:", type=("build", "run"))
	depends_on("r-pracma@2.2.5:", type=("build", "run"))
	depends_on("r-dbscan@1.1.5:", type=("build", "run"))
	depends_on("r-mmand@1.5.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-dittoseq", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
