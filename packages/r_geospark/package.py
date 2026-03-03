# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeospark(RPackage):
	"""Bring Local Sf to Spark

	R binds 'GeoSpark' <http://geospark.datasyslab.org/> extending 'sparklyr' 
    <https://spark.rstudio.com/> R package to make distributed 'geocomputing' easier. Sf is a
    package that provides [simple features] <https://en.wikipedia.org/wiki/Simple_Features> access
    for R and which is a leading 'geospatial' data processing tool. 'Geospark' R package bring 
    the same simple features access like sf but running on Spark distributed system.
	"""
	
	cran = "geospark" 

	version("0.3.1", md5="12a303fb9179365a7cd2bcc0349b5cde")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-sparklyr@1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-dbplyr@1.3:", type=("build", "run"))
