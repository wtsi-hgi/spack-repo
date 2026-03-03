# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssForeach(RPackage):
	"""Parallel Computations for Distributional Regression

	Computational intensive calculations for Generalized Additive Models for Location Scale and Shape, <doi:10.1111/j.1467-9876.2005.00510.x>. 
	"""
	
	homepage = "https://www.gamlss.com/"
	cran = "gamlss.foreach" 

	version("1.1-6", md5="374b1c30bcdb20505b5182e192fa29b1")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-gamlss-data", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
