# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInlcolor(RPackage):
	"""Color Schemes for the USGS Idaho National Laboratory Project
Office

	A collection of functions for creating color schemes.
    Used to support packages and scripts written
    by researchers at the United States Geological Survey (USGS)
    Idaho National Laboratory Project Office.
	"""
	
	homepage = "https://rconnect.usgs.gov/INLPO/inlcolor-main/"
	cran = "inlcolor" 

	version("1.0.6", md5="70b14c811f0dc05f016366f78e6cfd43")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
