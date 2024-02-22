# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeosimilarity(RPackage):
	"""Geographically Optimal Similarity

	Understanding spatial association is essential for spatial 
             statistical inference, including factor exploration and spatial prediction. 
             Geographically optimal similarity (GOS) model is an effective method 
             for spatial prediction, as described in Yongze Song (2022) 
             <doi:10.1007/s11004-022-10036-8>. GOS was developed based on 
             the geographical similarity principle, as described in Axing Zhu (2018) 
             <doi:10.1080/19475683.2018.1534890>. GOS has advantages in 
             more accurate spatial prediction using fewer samples and 
             critically reduced prediction uncertainty. 
	"""
	
	cran = "geosimilarity" 

	version("2.2", md5="b7ed726be7b73019e627159d83db3c14")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-secdim", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
