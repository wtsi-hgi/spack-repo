# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeojson(RPackage):
	"""Classes for 'GeoJSON'

	Classes for 'GeoJSON' to make working with 'GeoJSON' easier.
    Includes S3 classes for 'GeoJSON' classes with brief summary output,
    and a few methods such as extracting and adding bounding boxes,
    properties, and coordinate reference systems; working with 
    newline delimited 'GeoJSON'; and serializing to/from 'Geobuf' binary 'GeoJSON' 
    format.
	"""
	
	homepage = "https://docs.ropensci.org/geojson/"
	cran = "geojson" 

	version("0.3.5", md5="616e131632f8ccaddb64b367dc3e4f25")

	depends_on("r-sp", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-protolite@1.8:", type=("build", "run"))
	depends_on("r-jqr@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
