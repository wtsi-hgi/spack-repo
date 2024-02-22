# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlobe(RPackage):
	"""Plot 2D and 3D Views of the Earth, Including Major Coastline

	Basic functions for plotting 2D and 3D views of a sphere, by default the Earth with its major coastline, and additional lines and points. 
	"""
	
	cran = "globe" 

	version("1.2-0", md5="9e48ae0c2c7c362632c7c7c92a1d2222")

	depends_on("r@2.10:", type=("build", "run"))
