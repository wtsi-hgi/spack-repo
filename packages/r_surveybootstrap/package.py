# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveybootstrap(RPackage):
	"""Bootstrap with Survey Data

	Implements different kinds of bootstraps
    to estimate sampling variation from survey data with 
    complex designs. Includes the rescaled bootstrap
    described in Rust and Rao (1996) <doi:10.1177/096228029600500305> and
    Rao and Wu (1988) <doi:10.1080/01621459.1988.10478591>. 
	"""
	
	cran = "surveybootstrap" 

	version("0.0.3", md5="f92e4cb85c15996da7793017763c7608")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-functional", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
