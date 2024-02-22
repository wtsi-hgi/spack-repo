# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgo(RPackage):
	"""Simple Geographical Operations (with OSGB36)

	Methods focused in performing the OSGB36/ETRS89 transformation 
  (Great Britain and the Isle of Man only) by using the Ordnance Survey's 
  OSTN15/OSGM15 transformation model. Calculation of distances and areas from 
  sets of points defined in any of the supported Coordinated Systems is also
  available.
	"""
	
	homepage = "https://github.com/clozanoruiz/sgo"
	cran = "sgo" 

	version("0.9.2", md5="3e57319c581a71c159747673a9ded53c")

	depends_on("r@3.5:", type=("build", "run"))
