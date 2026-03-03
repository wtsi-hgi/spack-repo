# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCplm(RPackage):
	"""Compound Poisson Linear Models

	Likelihood-based and Bayesian methods for various compound Poisson linear models based on Zhang, Yanwei (2013) <doi:10.1007/s11222-012-9343-7>.
	"""
	
	homepage = "https://github.com/actuaryzhang/cplm"
	cran = "cplm" 

	version("0.7-12", md5="7e68360c5d12ae72a5d8054526152ab5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biglm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-tweedie", type=("build", "run"))
