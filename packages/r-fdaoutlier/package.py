# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdaoutlier(RPackage):
	"""Outlier Detection Tools for Functional Data Analysis

	A collection of functions for outlier detection in functional data analysis. 
  Methods implemented include directional outlyingness by 
  Dai and Genton (2019) <doi:10.1016/j.csda.2018.03.017>,
  MS-plot by Dai and Genton (2018) <doi:10.1080/10618600.2018.1473781>,
  total variation depth and modified shape similarity index by 
  Huang and Sun (2019) <doi:10.1080/00401706.2019.1574241>, and sequential transformations by
  Dai et al. (2020) <doi:10.1016/j.csda.2020.106960 among others. Additional outlier detection
  tools and depths for functional data like functional boxplot, (modified) band depth etc.,
  are also available. 
	"""
	
	homepage = "https://github.com/otsegun/fdaoutlier"
	cran = "fdaoutlier" 

	version("0.2.1", md5="a191f6030566fc8dbaae8837b4bd5801")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
