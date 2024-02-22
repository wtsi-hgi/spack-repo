# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdept(RPackage):
	"""Adaptive Empirical Pattern Transformation

	Designed for optimal use in performing fast, 
    accurate walking strides segmentation from high-density 
    data collected from a wearable accelerometer worn 
    during continuous walking activity.
	"""
	
	homepage = "https://github.com/martakarass/adept"
	cran = "adept" 

	version("1.2", md5="2ac4b08fdc25d0c06f6b3b85bbacac70")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dvmisc", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
