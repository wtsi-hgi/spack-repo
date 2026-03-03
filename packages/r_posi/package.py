# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPosi(RPackage):
	"""Valid Post-Selection Inference for Linear LS Regression

	
  In linear LS regression, calculate for a given design matrix
  the multiplier K of coefficient standard errors such that the
  confidence intervals [b - K*SE(b), b + K*SE(b)] have a
  guaranteed coverage probability for all coefficient estimates
  b in any submodels after performing arbitrary model selection.
	"""
	
	cran = "PoSI" 

	version("1.1", md5="84564b524ed3e6390473e44b4fea4aec")

