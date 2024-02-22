# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBezier(RPackage):
	"""Toolkit for Bezier Curves and Splines

	The bezier package is a toolkit for working with Bezier curves and splines. The package provides functions for point generation, arc length estimation, degree elevation and curve fitting.
	"""
	
	cran = "bezier" 

	version("1.1.2", md5="ff007027f4c27591f9b47bf43be8aaa1")

