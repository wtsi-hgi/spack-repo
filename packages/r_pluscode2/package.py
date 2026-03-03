# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPluscode2(RPackage):
	"""Coordinates to 'Plus Code' Conversion Tool

	Generates 'Plus Code' of geometric objects or data frames that contain them, giving the possibility to specify the precision of the area. The main feature of the package comes from the open-source code developed by 'Google Inc.' present in the repository <https://github.com/google/open-location-code/blob/main/java/src/main/java/com/google/openlocationcode/OpenLocationCode.java>. For details about 'Plus Code', visit <https://maps.google.com/pluscodes/> or <https://github.com/google/open-location-code>.
	"""
	
	homepage = "https://github.com/Armando-d/plusCode2"
	cran = "plusCode2" 

	version("0.1.0", md5="07e5198f2f175a4c7789ee6611351b17", url="https://cran.r-project.org/src/contrib/plusCode2_0.1.0.tar.gz")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
