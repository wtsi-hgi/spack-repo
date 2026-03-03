# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMandelbrot(RPackage):
	"""Generates Views on the Mandelbrot Set

	Estimates membership for the Mandelbrot set.
	"""
	
	cran = "mandelbrot" 

	version("0.2.0", md5="7536da2114f6452ad0bd2db2d10db968")

	depends_on("r-reshape2", type=("build", "run"))
