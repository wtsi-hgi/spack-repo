# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnapkrig(RPackage):
	"""Fast Kriging and Geostatistics on Grids with Kronecker
Covariance

	Geostatistical modeling and kriging with
    gridded data using spatially separable covariance functions (Kronecker
    covariances). Kronecker products in these models provide shortcuts for
    solving large matrix problems in likelihood and conditional mean,
    making 'snapKrig' computationally efficient with large grids. The package
    supplies its own S3 grid object class, and a host of methods including
    plot, print, Ops, square bracket replace/assign, and more. Our computational
    methods are described in Koch, Lele, Lewis (2020) <doi:10.7939/r3-g6qb-bq70>.
	"""
	
	homepage = "https://github.com/deankoch/snapKrig"
	cran = "snapKrig" 

	version("0.0.2", md5="a96eff9633e132d8d247d866557ca840")

