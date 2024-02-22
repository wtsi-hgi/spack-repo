# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeospt(RPackage):
	"""Geostatistical Analysis and Design of Optimal Spatial Sampling
Networks

	Estimation of the variogram through trimmed mean, radial basis 
        functions (optimization, prediction and cross-validation), summary
        statistics from cross-validation, pocket plot, and design of
        optimal sampling networks through sequential and simultaneous
        points methods.
	"""
	
	homepage = "https://github.com/amsantac/geospt"
	cran = "geospt" 

	version("1.0-4", md5="fb5829a833802c5ed8cb2e50f641b4b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-genalg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-sgeostat", type=("build", "run"))
