# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrimetstops(RPackage):
	"""Information on all of the TriMet Stops in the Portland Metro
Area

	Information on all of the TriMet stops in the Portland Metro Area. It includes information such as the longitude, latitude, cross street, and direction of the stop. TriMet has catalogued these stops, 6880 in total. 
	"""
	
	homepage = "https://github.com/graysonwhite/trimetStops"
	cran = "trimetStops" 

	version("0.1.0", md5="c063eb84eb890dba7627a0b192580bb2")

	depends_on("r@3.1:", type=("build", "run"))
