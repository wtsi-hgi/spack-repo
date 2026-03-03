# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMba(RPackage):
	"""Multilevel B-Spline Approximation

	Functions to interpolate irregularly and regularly spaced data using Multilevel B-spline Approximation (MBA). Functions call portions of the SINTEF Multilevel B-spline Library written by Øyvind Hjelle which implements methods developed by Lee, Wolberg and Shin (1997; <doi:10.1109/2945.620490>).
	"""
	
	cran = "MBA" 

	version("0.1-0", md5="8b0a70701c0a153352088e320d0204df")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
