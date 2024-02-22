# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpherepc(RPackage):
	"""Spherical Principal Curves

	Fitting dimension reduction methods to data lying on two-dimensional sphere.
    This package provides principal geodesic analysis, principal circle, principal curves 
    proposed by Hauberg, and spherical principal curves. Moreover, it offers the method of locally   
    defined principal geodesics which is underway. The detailed procedures 
    are described in Lee, J., Kim, J.-H. and Oh, H.-S. (2021) <doi:10.1109/TPAMI.2020.3025327>. 
    Also see Kim, J.-H., Lee, J. and Oh, H.-S. (2020) <arXiv:2003.02578>.
	"""
	
	cran = "spherepc" 

	version("0.1.7", md5="5af572742424da411c922e933e847eb0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-sphereplot", type=("build", "run"))
