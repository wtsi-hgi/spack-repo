# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQualitycontrol(RPackage):
	"""Unified Framework for Data Quality Control

	An easy framework to set a quality control workflow on a dataset.
  Includes a various range of functions that allow to establish an adaptable 
  data quality control.
	"""
	
	homepage = "https://github.com/luisgarcez11/qualitycontrol"
	cran = "qualitycontrol" 

	version("0.1.0", md5="e6371d45797218f3b33748372a41d3a9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
