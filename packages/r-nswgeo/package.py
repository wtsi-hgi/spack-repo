# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNswgeo(RPackage):
	"""Geospatial Data and Maps for New South Wales, Australia

	Geospatial data for creating maps of New South Wales (NSW),
  Australia, and some helpers to work with common problems like normalising
  postcodes. Registers its data with 'cartographer'.
	"""
	
	homepage = "https://github.com/cidm-ph/nswgeo"
	cran = "nswgeo" 

	version("0.4.0", md5="ba95c3408ec21c687a105fc43692959b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cartographer@0.2:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
