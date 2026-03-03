# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTracenma(RPackage):
	"""Database for Developing Transitivity Methodology in Network
Meta-Analysis

	Functions to access the database of 217 data-frames with aggregate 
    study-level characteristics (that may act as effect modifiers) extracted 
    from published systematic reviews with network meta-analysis. The database shall 
    only be used for developing and appraising the methodology to assess 
    the transitivity assumption quantitatively.
	"""
	
	homepage = "https://CRAN.R-project.org/package=tracenma"
	cran = "tracenma" 

	version("0.1.0", md5="a3e53bc57ab41f15adb711be533ab712")

	depends_on("r@4:", type=("build", "run"))
