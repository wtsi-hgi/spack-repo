# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItcsegment(RPackage):
	"""Individual Tree Crowns Segmentation

	Three methods for Individual Tree Crowns (ITCs) delineation on remote sensing data: one is based on LiDAR data in x,y,z format and one on imagery data in raster format.
	"""
	
	cran = "itcSegment" 

	version("1.0", md5="df93382b66bf2b5238fd3d6ed50f6c75")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
