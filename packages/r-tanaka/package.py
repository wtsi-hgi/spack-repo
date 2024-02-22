# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTanaka(RPackage):
	"""Design Shaded Contour Lines (or Tanaka) Maps

	The Tanaka method enhances the representation of topography on
    a map using shaded contour lines. In this simplified implementation of
    the method, north-west white contours represent illuminated topography
    and south-east black contours represent shaded topography. See Tanaka
    (1950) <doi:10.2307/211219>.
	"""
	
	homepage = "https://github.com/riatelab/tanaka/"
	cran = "tanaka" 

	version("0.4.0", md5="b617ff622c772144ed4bdf7dbfbdb880")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-mapiso", type=("build", "run"))
	depends_on("r-maplegend", type=("build", "run"))
