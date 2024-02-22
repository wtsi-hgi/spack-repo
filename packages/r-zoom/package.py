# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZoom(RPackage):
	"""A Spatial Data Visualization Tool

	You can call zm(), when displaying any active plot to enter an
    interactive session to zoom/navigate any plot. The development
    version, as well as binary releases can be found at
    <https://github.com/cbarbu/R-package-zoom>. 
	"""
	
	homepage = "https://github.com/cbarbu/R-package-zoom"
	cran = "zoom" 

	version("2.0.6", md5="10971cd4ca0e6df803dd99138f428cb6")

	depends_on("r@2.10:", type=("build", "run"))
