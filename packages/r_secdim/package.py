# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecdim(RPackage):
	"""The Second Dimension of Spatial Association

	Most of the current methods explore spatial association using 
             observations at sample locations, which are defined as the first 
             dimension of spatial association (FDA). The proposed concept of
             the second dimension of spatial association (SDA), 
             as described in Yongze Song (2022) 
             <doi:10.1016/j.jag.2022.102834>, aims to extract
             in-depth information about the geographical environment from 
             locations outside sample locations for exploring spatial
             association. 
	"""
	
	cran = "SecDim" 

	version("3.2", md5="7c63b81e7d4ffd8130c3f847820262cb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
