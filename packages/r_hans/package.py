# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHans(RPackage):
	"""Haversines are not Slow

	The haversine is a function used to calculate the distance between a pair of 
    latitude and longitude points while accounting for the assumption that the points 
    are on a spherical globe. This package provides a fast, dataframe compatible, 
    haversine function. For the first publication on the haversine calculation see 
    Joseph de Mendoza y Ríos (1795) <https://books.google.cat/books?id=030t0OqlX2AC> (In Spanish).
	"""
	
	cran = "hans" 

	version("0.1", md5="2050c82ddd4e290c63b7c46550065512")

	depends_on("r-rcpp", type=("build", "run"))
