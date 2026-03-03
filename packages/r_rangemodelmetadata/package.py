# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRangemodelmetadata(RPackage):
	"""Provides Templates for Metadata Files Associated with Species
Range Models

	Range Modeling Metadata Standards (RMMS) address three challenges: 
  they (i) are designed for convenience to encourage use, (ii) accommodate a wide 
  variety of applications, and (iii) are extensible to allow the community of range 
  modelers to steer it as needed. RMMS are based on a data dictionary that specifies 
  a hierarchical structure to catalog different aspects of the range modeling process. 
  The dictionary balances a constrained, minimalist vocabulary to improve 
  standardization with flexibility for users to provide their own values. 
  Merow et al. (2019) <DOI:10.1111/geb.12993> describe the standards in 
  more detail. Note that users who prefer to use the R package 'ecospat' can obtain it from
  <https://github.com/ecospat/ecospat>.
	"""
	
	cran = "rangeModelMetadata" 

	version("0.1.5", md5="b331c78cf37ecc4fb645571a27d4aa95")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-spocc", type=("build", "run"))
	depends_on("r-bien", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
