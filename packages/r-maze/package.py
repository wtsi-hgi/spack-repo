# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaze(RPackage):
	"""Mediation Analysis for Zero-Inflated Mediators

	A novel mediation analysis approach to address zero-inflated mediators containing true zeros and false zeros. See Jiang et al (2023) "A Novel Causal Mediation Analysis Approach for Zero-Inflated Mediators" <arXiv:2301.10064> for more details.
	"""
	
	homepage = "https://github.com/meilinjiang/MAZE"
	cran = "MAZE" 

	version("0.0.2", md5="70e25928394e58f82b60f97e2d804bd8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
