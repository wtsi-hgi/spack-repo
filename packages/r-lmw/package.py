# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmw(RPackage):
	"""Linear Model Weights

	Computes the implied weights of linear regression models for estimating
     average causal effects and provides diagnostics based on these weights. These
     diagnostics rely on the analyses in Chattopadhyay and Zubizarreta (2023)
     <doi:10.1093/biomet/asac058> where
     several regression estimators are represented as weighting estimators, in connection
     to inverse probability weighting. 'lmw' provides tools to diagnose
     representativeness, balance, extrapolation, and influence for these models,
     clarifying the target population of inference. Tools are also available to
     simplify estimating treatment effects for specific target populations of interest.
	"""
	
	homepage = "https://github.com/ngreifer/lmw"
	cran = "lmw" 

	version("0.0.2", md5="e53c7c0a3110a40226bb9601a4cbe416")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chk@0.9.1:", type=("build", "run"))
	depends_on("r-sandwich@3.0.2:", type=("build", "run"))
	depends_on("r-backports@1.4.1:", type=("build", "run"))
