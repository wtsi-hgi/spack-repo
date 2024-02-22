# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImagefx(RPackage):
	"""Extract Features from Images

	Synthesize images into characteristic features for time-series analysis or machine learning applications.  The package was originally intended for monitoring volcanic eruptions in video data by highlighting and extracting regions above the vent associated with plume activity.  However, the functions within are general and have wide applications for image processing, analyzing, filtering, and plotting.       
	"""
	
	cran = "imagefx" 

	version("0.4.1", md5="78898f658c38024e865472f093352197")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
