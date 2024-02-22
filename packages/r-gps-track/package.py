# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpsTrack(RPackage):
	"""GPS Track Point Information Extractor

	Focused on extracting important data from track points such as speed, distance, elevation difference and azimuth.(PLAZA, J. et al., 2022) <doi:10.1016/j.applanim.2022.105643>.
	"""
	
	cran = "gps.track" 

	version("1.0.0", md5="4b86b2e06d759dbad9bf421866b89b41")

	depends_on("r-nngeo", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
