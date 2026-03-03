# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothic(RPackage):
	"""Variable Selection Using a Smooth Information Criterion

	Implementation of the SIC epsilon-telescope method, either
    using single or distributional (multiparameter) regression. Includes classical regression
    with normally distributed errors and robust regression, where the errors are from
    the Laplace distribution. The "smooth generalized normal distribution" is used,
    where the estimation of an additional shape parameter allows the user to move
    smoothly between both types of regression. See O'Neill and Burke (2022)
    "Robust Distributional Regression with Automatic Variable Selection" for more details.
    <arXiv:2212.07317>. This package also contains the data analyses from O'Neill and
    Burke (2023). "Variable selection using a smooth information criterion for distributional
    regression models". <doi:10.1007/s11222-023-10204-8>.
	"""
	
	homepage = "https://github.com/meadhbh-oneill/smoothic"
	cran = "smoothic" 

	version("1.2.0", md5="0c0fcbfd1c0dae3f7bbdc3c8161e6eea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-toordinal", type=("build", "run"))
