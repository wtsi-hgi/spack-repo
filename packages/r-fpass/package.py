# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpass(RPackage):
	"""Power and Sample Size for Projection Test under Repeated
Measures

	Computes the power and sample size (PASS) required to test for the
    difference in the mean function between two groups under a repeatedly measured longitudinal 
    or sparse functional design. See the manuscript by Koner and Luo (2023) <https://salilkoner.github.io/assets/PASS_manuscript.pdf> 
    for details of the PASS formula and computational details. The details of the testing
    procedure for univariate and multivariate response are presented in
    Wang (2021) <doi:10.1214/21-EJS1802> and Koner and Luo (2023) 
    <arXiv:2302.05612> respectively. 
	"""
	
	homepage = "https://github.com/SalilKoner/fPASS"
	cran = "fPASS" 

	version("1.0.0", md5="830c9c83b38fe47ca89592dae1646cd9")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-face", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
	depends_on("r-gss", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
