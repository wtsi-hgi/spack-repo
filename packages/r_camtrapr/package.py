# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCamtrapr(RPackage):
	"""Camera Trap Data Management and Preparation of Occupancy and
Spatial Capture-Recapture Analyses

	Management of and data extraction from camera trap data in wildlife studies. The package provides a workflow for storing and sorting camera trap photos (and videos), tabulates records of species and individuals, and creates detection/non-detection matrices for occupancy and spatial capture-recapture analyses with great flexibility. In addition, it can visualise species activity data and provides simple mapping functions with GIS export.
	"""
	
	homepage = "https://github.com/jniedballa/camtrapR"
	cran = "camtrapR" 

	version("2.3.0", md5="72a4b9740caf14d93414592b26a1b693")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-secr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
