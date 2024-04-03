# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialml(RPackage):
	"""Spatial Machine Learning

	Implements a spatial extension of the random forest algorithm 
             (Georganos et al. (2019) <doi:10.1080/10106049.2019.1595177>).
             Allows for a geographically weighted random forest regression 
             including a function to find the optical bandwidth. (Georganos 
             and Kalogirou (2022) <https://www.mdpi.com/2220-9964/11/9/471>).
	"""
	
	homepage = "https://stamatisgeoai.eu/"
	cran = "SpatialML" 

	version("0.1.7", md5="f894a29104b6dc2ea7c3c0acb1002de9")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ranger@0.15.1:", type=("build", "run"))
	depends_on("r-caret@6:", type=("build", "run"))
	depends_on("r-randomforest@4.7:", type=("build", "run"))
