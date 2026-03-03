# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRisksimul(RPackage):
	"""Risk Quantification for Stock Portfolios under the T-Copula
Model

	Implements efficient simulation procedures to estimate tail loss probabilities and conditional excess for a stock portfolio. The log-returns are assumed to follow a t-copula model with generalized hyperbolic or t marginals. 
	"""
	
	cran = "riskSimul" 

	version("0.1.2", md5="ca2dbf16f3f3768de19c99ec8865ebe9")

	depends_on("r-runuran", type=("build", "run"))
