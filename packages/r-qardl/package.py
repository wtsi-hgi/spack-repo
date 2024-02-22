# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQardl(RPackage):
	"""Quantile Autoregressive Distributed Lag Model

	Compute the quantile autoregressive distributed lag model  of Cho, Jin Seo & Kim, Tae-hwan & Shin, Yongcheol,(2015) <DOI:10.1016/j.jeconom.2015.05.003> and the short and long-run wald tests.
	"""
	
	cran = "Qardl" 

	version("0.1.1", md5="26de5984e403145029f0d6f54e67be0d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
