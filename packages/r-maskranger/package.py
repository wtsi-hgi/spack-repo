# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaskranger(RPackage):
	"""Mask Species Geographic Ranges

	Mask ranges based on expert 
    knowledge or remote sensing layers. These tools can 
    be combined to quantitatively and reproducibly 
    generate a new map or to update an existing map.
    Methods include expert opinion and data-driven 
    tools to generate thresholds for binary masks.
	"""
	
	cran = "maskRangeR" 

	version("1.1", md5="70c3bb75535c17a3fa028ad57215c055")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
