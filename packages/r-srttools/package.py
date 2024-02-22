# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrttools(RPackage):
	"""Adjust Srt File to Get Better Experience when Watching Movie

	Srt file is a common subtitle format for videos, it contains subtitle and when the subtitle showed.
    This package is for align time of srt file, and also change color, style and position of subtitle in videos,
	the srt file will be read as a vector into R, and can be write into srt file after modified using this package.
	"""
	
	homepage = "https://github.com/ChiHangChen/SRTtools"
	cran = "SRTtools" 

	version("1.2.0", md5="770002a063aebc2f954cf4c983be24cf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
