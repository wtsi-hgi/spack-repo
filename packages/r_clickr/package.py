# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClickr(RPackage):
	"""Semi-Automatic Preprocessing of Messy Data with Change Tracking
for Dataset Cleaning

	Tools for assessing data quality, performing exploratory analysis, and 
    semi-automatic preprocessing of messy data with change tracking for integral dataset cleaning.
	"""
	
	cran = "clickR" 

	version("0.9.39", md5="692a2a2fde7f8c1cfe97b7cd30474113")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-beeswarm", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
