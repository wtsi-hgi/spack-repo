# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsgarchelm(RPackage):
	"""Hybridization of MS-GARCH and ELM Model

	Implements the three parallel forecast combinations of Markov Switching GARCH and extreme learning machine model along with the selection of appropriate model for volatility forecasting. For method details see Hsiao C, Wan SK (2014). <doi:10.1016/j.jeconom.2013.11.003>, Hansen BE (2007). <doi:10.1111/j.1468-0262.2007.00785.x>, Elliott G, Gargano A, Timmermann A (2013). <doi:10.1016/j.jeconom.2013.04.017>. 
	"""
	
	cran = "MSGARCHelm" 

	version("0.1.0", md5="62b8c75d1dcc9e01c2f161b64459d7b1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nnfor", type=("build", "run"))
	depends_on("r-msgarch", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
