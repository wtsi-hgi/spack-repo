# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHs(RPackage):
	"""Homogenous Segmentation for Spatial Lines Data

	Methods of homogenous segmentation for spatial lines data, such as pavement 
             performance indicators and traffic volumes. Three methods are available for 
             homogenous segmentation, including cumulative difference approach, minimization 
             coefficient of variation, and spatial heterogeneity based method.  
	"""
	
	cran = "HS" 

	version("1.1", md5="493dd39d7814fd27eeee72448a5c74ca")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
