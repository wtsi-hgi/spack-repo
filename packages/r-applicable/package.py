# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApplicable(RPackage):
	"""A Compilation of Applicability Domain Methods

	A modeling package compiling applicability domain methods in
    R. It combines different methods to measure the amount of
    extrapolation new samples can have from the training set. See Gadaleta et 
    al (2016)  <doi:10.4018/IJQSPR.2016010102> for an overview of
    applicability domains.
	"""
	
	homepage = "https://github.com/tidymodels/applicable"
	cran = "applicable" 

	version("0.1.0", md5="95cede7e0bdcb5cf9df777df2539696b")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hardhat@0.1.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-proxyc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
