# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevgeo(RPackage):
	"""Reverse Geocoding with the Photon Geocoder for OpenStreetMap,
Google Maps, and Bing

	Function revgeo() allows you to use the Photon geocoder for OpenStreetMap <http://photon.komoot.de>, Google Maps <http://maps.google.com>, and Bing <https://www.bingmapsportal.com> to reverse geocode coordinate pairs with minimal hassle. 
	"""
	
	cran = "revgeo" 

	version("0.15", md5="3db5b6cb1dc629f64426bb98fe9978d2")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-rcurl@1.95:", type=("build", "run"))
	depends_on("r-rjsonio@1.3.0:", type=("build", "run"))
