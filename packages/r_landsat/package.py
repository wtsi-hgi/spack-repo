# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandsat(RPackage):
	"""Radiometric and Topographic Correction of Satellite Imagery

	Processing of Landsat or other multispectral satellite imagery. Includes relative normalization, image-based radiometric correction, and topographic correction options. The original package description was published as Goslee (2011) <doi:10.18637/jss.v043.i04>, and details of the topographic corrections in Goslee (2012) <doi:10.14358/PERS.78.9.973>.
	"""
	
	cran = "landsat" 

	version("1.1.2", md5="6f41f3005e83ee80fa6792c198fedd82")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-sp@2:", type=("build", "run"))
	depends_on("r-lmodel2", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
