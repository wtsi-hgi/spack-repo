# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenmmi(RPackage):
	"""Benthic Multi-Metric Index

	Analysis tool for evaluating benthic multimetric indices (BENMMIs). 
    It generates reproducible reports on the analysis of benthic data, e.g., 
    validation and correction of species names, sample pooling, automatic
    conversion of genus to species names, outlier detection, benthic 
    indicator calculation, optimization of single and 
    multimetric indicators against a pressure gradient, and spatial aggregation
    of benthic indicators. One of its use cases was the development of a common 
    benthic indicator for <https://www.ospar.org> (publication accepted by 
    Ecological Indicators). See Van Loon et al. (2018) <doi:10.1016/j.ecolind.2017.09.029> for details. 
	"""
	
	cran = "BENMMI" 

	version("4.3-7", md5="9e46118d05dc57b7a2bc8447e01ec9a1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-benthos@1.3.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
