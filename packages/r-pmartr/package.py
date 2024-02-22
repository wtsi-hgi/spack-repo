# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmartr(RPackage):
	"""Panomics Marketplace - Quality Control and Statistical Analysis
for Panomics Data

	Provides functionality for quality control processing and statistical analysis of mass spectrometry (MS) omics data, in particular proteomic (either at the peptide or the protein level), lipidomic, and metabolomic data, as well as RNA-seq based count data and nuclear magnetic resonance (NMR) data. This includes data transformation, specification of groups that are to be compared against each other, filtering of features and/or samples, data normalization, data summarization (correlation, PCA), and statistical comparisons between defined groups.  Implements methods described in:  Webb-Robertson et al. (2014) <doi:10.1074/mcp.M113.030932>.  Webb-Robertson et al. (2011) <doi:10.1002/pmic.201100078>.  Matzke et al. (2011) <doi:10.1093/bioinformatics/btr479>.  Matzke et al. (2013) <doi:10.1002/pmic.201200269>.  Polpitiya et al. (2008) <doi:10.1093/bioinformatics/btn217>.  Webb-Robertson et al. (2010) <doi:10.1021/pr1005247>.  
	"""
	
	homepage = "https://github.com/pmartR/pmartR"
	cran = "pmartR" 

	version("2.4.2", md5="ae34ffd49b1a2d3ddd4cc0f85b288033")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-glmpca", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
