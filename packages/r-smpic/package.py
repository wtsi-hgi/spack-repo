# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmpic(RPackage):
	"""Creates Images Sized for Social Media

	Creates images that are the proper size for social media. Beautiful
    plots, charts and graphs wither and die if they are not shared. Social media 
    is perfect for this but every platform has its own image dimensions. With 
    'smpic' you can easily save your plots with the exact dimensions needed for 
    the different platforms.
	"""
	
	homepage = "https://github.com/mikkelkrogsholm/smpic"
	cran = "smpic" 

	version("0.1.0", md5="06583900101303dc3094b07fbbffae9f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
