# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDraw(RPackage):
	"""Wrapper Functions for Producing Graphics

	A set of user-friendly wrapper functions for creating consistent graphics and diagrams with lines, common shapes, text, and page settings.
  Compatible with and based on the R 'grid' package.
	"""
	
	homepage = "https://github.com/rrwen/draw"
	cran = "draw" 

	version("1.0.0", md5="3f35a9579eeeb650732962f40cdfb03a")

