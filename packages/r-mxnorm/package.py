# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMxnorm(RPackage):
	"""Apply Normalization Methods to Multiplexed Images

	Implements methods to normalize multiplexed imaging data, including
    statistical metrics and visualizations to quantify technical variation in 
    this data type. Reference for methods listed here: Harris, C., Wrobel, J., 
    & Vandekar, S. (2022). mxnorm: An R Package to Normalize Multiplexed Imaging 
    Data. Journal of Open Source Software, 7(71), 4180, 
    <doi:10.21105/joss.04180>.
	"""
	
	cran = "mxnorm" 

	version("1.0.3", md5="ecb606bbfd48493818cd51458b948df0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-fossil", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
