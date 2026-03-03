# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmcc(RPackage):
	"""Airborne LiDAR Filtering Method Based on Multiscale Curvature

	Multiscale Curvature Classification of ground returns in 3-D LiDAR 
    point clouds, designed for forested environments. 'RMCC' is a porting to R of the 
    'MCC-lidar' method by Evans and Hudak (2007) <doi:10.1109/TGRS.2006.890412>.
	"""
	
	cran = "RMCC" 

	version("0.1.0", md5="0b4faa6e9e6617b0ffe5b591521fa460")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
