# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdimnormn(RPackage):
	"""Multi-Dimensional MA Normalization for Plate Effect

	Normalize data to minimize the difference between sample plates 
    (batch effects). For given data in a matrix and grouping variable (or
	plate), the function 'normn_MA' normalizes the data on MA coordinates. 
	More details are in the citation. The primary method is 'Multi-MA'. Other 
	fitting functions on MA coordinates can also be employed e.g. loess.  
	"""
	
	cran = "MDimNormn" 

	version("0.8.0", md5="236e265dd384a82c2554aec892053b8a")

	depends_on("r@3.2:", type=("build", "run"))
