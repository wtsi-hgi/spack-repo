# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexcwm(RPackage):
	"""Flexible Cluster-Weighted Modeling

	Allows maximum likelihood fitting of cluster-weighted models, a class of mixtures of regression models with random covariates. 
            Methods are described in Angelo Mazza, Antonio Punzo, Salvatore Ingrassia (2018) <doi:10.18637/jss.v086.i02>.
	"""
	
	cran = "flexCWM" 

	version("1.92", md5="85c36f8f20877df05780fa48e5387b47")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-contaminatedmixt", type=("build", "run"))
