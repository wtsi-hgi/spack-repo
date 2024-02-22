# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpi(RPackage):
	"""Conditional Predictive Impact

	A general test for conditional independence in supervised learning 
  algorithms as proposed by Watson & Wright (2021) <doi:10.1007/s10994-021-06030-6>. 
  Implements a conditional variable importance measure which can be applied to any supervised 
  learning algorithm and loss function. Provides statistical inference procedures without 
  parametric assumptions and applies equally well to continuous and categorical predictors 
  and outcomes.
	"""
	
	homepage = "https://github.com/bips-hb/cpi"
	cran = "cpi" 

	version("0.1.4", md5="c8c58dfe64b32e118dbb809524507282")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mlr3", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-knockoff", type=("build", "run"))
