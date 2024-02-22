# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeoelectrics(RPackage):
	"""3D-Visualization of Geoelectric Resistivity Measurement Profiles

	Visualizes two-dimensional geoelectric resistivity measurement profiles in three dimensions.
	"""
	
	homepage = "https://github.com/kleebaum/geoelectrics"
	cran = "geoelectrics" 

	version("0.2.2", md5="c95535171ca03f65f3f45dec8775123d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
