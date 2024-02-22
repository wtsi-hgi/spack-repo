# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgeostat(RPackage):
	"""An Object-Oriented Framework for Geostatistical Modeling in S+

	An Object-oriented Framework for Geostatistical Modeling in S+ 
  containing functions for variogram estimation, variogram fitting and kriging
  as well as some plot functions. Written entirely in S, therefore works only
  for small data sets in acceptable computing time.
	"""
	
	cran = "sgeostat" 

	version("1.0-27", md5="0d1b7caa41af627124796a22d3141f12")

	depends_on("r@2:", type=("build", "run"))
