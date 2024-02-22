# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrackreconstruction(RPackage):
	"""Reconstruct Animal Tracks from Magnetometer, Accelerometer,
Depth and Optional Speed Data

	Reconstructs animal tracks from magnetometer, accelerometer, depth and optional speed data.  Designed primarily using data from Wildlife Computers Daily Diary tags deployed on northern fur seals.
	"""
	
	cran = "TrackReconstruction" 

	version("1.3", md5="db068bcc7e2ae8f9e986557297eeaae4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
