# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlookr(RPackage):
	"""Tools for Data Diagnosis, Exploration, Transformation

	A collection of tools that support data diagnosis, exploration, and transformation. 
    Data diagnostics provides information and visualization of missing values, outliers, and unique 
    and negative values to help you understand the distribution and quality of your data. 
    Data exploration provides information and visualization of the descriptive statistics of 
    univariate variables, normality tests and outliers, correlation of two variables, 
    and the relationship between the target variable and predictor. Data transformation supports binning 
    for categorizing continuous variables, imputes missing values and outliers, and resolves skewness. 
    And it creates automated reports that support these three tasks.
	"""
	
	homepage = "https://github.com/choonghyunryu/dlookr/"
	cran = "dlookr" 

	version("0.6.3", md5="a8dbd9cfd72dc0d1e7670e6811a32d0c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-showtext@0.9.4:", type=("build", "run"))
	depends_on("r-sysfonts@0.7.1:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hrbrthemes@0.8:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr@1.22:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-pagedown@0.15:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
