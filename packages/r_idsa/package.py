# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdsa(RPackage):
	"""An Interactive Detector for Spatial Associations

	Method of interactive detector for spatial associations (IDSA) 
             as described in Yongze Song (2021) <doi:10.1080/13658816.2021.1882680>. 
             IDSA is used to quantify the power of interactive determinant (PID) 
             between a spatial response variable and explanatory variables. 
             IDSA is developed based on methods of spatial heterogeneity. 
	"""
	
	cran = "IDSA" 

	version("2.1", md5="3e96dfd30d6de929e233054347d87d9a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gd", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
