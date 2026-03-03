# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemipar(RPackage):
	"""Semiparametic Regression

	Functions for semiparametric regression analysis, to
        complement the book: Ruppert, D., Wand, M.P. and Carroll, R.J.
        (2003). Semiparametric Regression. Cambridge University Press.
	"""
	
	homepage = "http://matt-wand.utsacademics.info/SPmanu.pdf"
	cran = "SemiPar" 

	version("1.0-4.2", md5="8ce41e57378e7a3ef21fd9b6a33c3a3d")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
