# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRabr(RPackage):
	"""Simulations for Response Adaptive Block Randomization Design

	Conduct simulations of the Response Adaptive Block Randomization (RABR) design to evaluate its type I error rate, power and operating characteristics for binary and continuous endpoints. For more details of the proposed method, please refer to Zhan et al. (2021) <doi:10.1002/sim.9104>. 
	"""
	
	homepage = "https://github.com/tian-yu-zhan/RABR"
	cran = "RABR" 

	version("0.1.1", md5="6c92b67f016ff935db9db712bd67abe1")

	depends_on("r-asd", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-multxpert", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
