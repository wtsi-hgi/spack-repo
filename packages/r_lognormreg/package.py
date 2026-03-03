# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLognormreg(RPackage):
	"""log Normal Linear Regression

	Functions to fits simple linear regression models with log normal errors 
		and identity link, i.e. taking the responses on the original scale. See
		Muggeo (2018) <doi:10.13140/RG.2.2.18118.16965>.
	"""
	
	cran = "logNormReg" 

	version("0.5-0", md5="085a84c2a9e6d6c4c5ed87e063f0b42c")

	depends_on("r@3.5:", type=("build", "run"))
