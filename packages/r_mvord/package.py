# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvord(RPackage):
	"""Multivariate Ordinal Regression Models

	A flexible framework for fitting multivariate
    ordinal regression models with composite likelihood methods. Methodological details are given in Hirk, Hornik, Vana (2020) <doi:10.18637/jss.v093.i04>.
	"""
	
	cran = "mvord" 

	version("1.2.2", md5="47087b59f0bf8eb84fb96918a41bb0c3")
	version("1.2.1", md5="9dcd8966357856ab51a8a6ef135bedac")

	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
