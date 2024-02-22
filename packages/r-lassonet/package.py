# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLassonet(RPackage):
	"""3CoSE Algorithm

	Contains functions to estimate a penalized regression model using 3CoSE algorithm, see Weber, Striaukas, Schumacher Binder (2018) <doi:10.2139/ssrn.3211163>.
	"""
	
	cran = "LassoNet" 

	version("0.8.3", md5="da1ffb7866c8f1bcdc61cfe462428ca0")

	depends_on("r-rcpp", type=("build", "run"))
