# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlreg(RPackage):
	"""Higher Order Inference for Nonlinear Heteroscedastic Models

	Likelihood inference based on higher order approximations 
  for nonlinear models with possibly non constant variance.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "nlreg" 

	version("1.2-2.2", md5="a6837cb43f7994d8aa4677a3b80cf2dc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
