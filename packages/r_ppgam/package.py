# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpgam(RPackage):
	"""Generalised Additive Point Process Models

	Methods for fitting point processes with parameters of generalised additive 
      model (GAM) form are provided. For an introduction to point processes see Cox, D.R & 
      Isham, V. (Point Processes, 1980, CRC Press), GAMs see Wood, S.N. (2017) 
      <doi:10.1201/9781315370279>, and the fitting approach see Wood, S.N., Pya, N. & 
      Safken, B. (2016) <doi:10.1080/01621459.2016.1180986>.
	"""
	
	cran = "ppgam" 

	version("1.0.1", md5="3652651c476f08405a422a0ecd230eb5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-evgam", type=("build", "run"))
