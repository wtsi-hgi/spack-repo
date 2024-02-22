# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTatoo(RPackage):
	"""Combine and Export Data Frames

	
  Functions to combine data.frames in ways that require additional effort in 
  base R, and to add metadata (id, title, ...) that can be used for printing and 
  xlsx export. The 'Tatoo_report' class is provided as a 
  convenient helper to write several such tables to a workbook, one table per 
  worksheet. Tatoo is built on top of 'openxlsx', but intimate knowledge of 
  that package is not required to use tatoo.
	"""
	
	homepage = "https://github.com/statistikat/tatoo"
	cran = "tatoo" 

	version("1.1.2", md5="efe43ae4b702e6e32cedd859d2b3dcc9")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-openxlsx@4:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-colt", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
