# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootct(RPackage):
	"""Bootstrapping the ARDL Tests for Cointegration

	The bootstrap ARDL tests for cointegration is the main functionality of this package. It also acts as a wrapper of the most commond ARDL testing procedures for cointegration: the bound tests of Pesaran, Shin and Smith (PSS; 2001 - <doi:10.1002/jae.616>) and the asymptotic test on the independent variables of Sam, McNown and Goh (SMG: 2019 - <doi:10.1016/j.econmod.2018.11.001>). Bootstrap and bound tests are performed under both the conditional and unconditional ARDL models.
	"""
	
	cran = "bootCT" 

	version("2.1.0", md5="8e139b7cf8f827c1fdfd2a17cc3998ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-ardl", type=("build", "run"))
	depends_on("r-dynamac", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
