# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialacc(RPackage):
	"""Spatial Accessibility Measures

	Provides a set of spatial accessibility measures from a set of locations 
             (demand) to another set of locations (supply). It aims, among others, 
             to support research on spatial accessibility to health care facilities. 
             Includes the locations and some characteristics of major public hospitals in Greece.
	"""
	
	homepage = "https://stamatisgeoai.eu/"
	cran = "SpatialAcc" 

	version("0.1-5", md5="8944249101fbd74dc47e5cc0311ea55d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
