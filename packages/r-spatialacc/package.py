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
	
	homepage = "http://lctools.science/"
	cran = "SpatialAcc" 

	version("0.1-4", md5="7ea815955beefa46235c5b48b1eafec0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
