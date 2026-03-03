# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriangulation(RPackage):
	"""Determine Position of Observer

	Measuring angles between points in a landscape is much easier
    than measuring distances. When the location of three points is known the
    position of the observer can be determined based solely on the angles between
    these points as seen by the observer. This task (known as triangulation)
    however requires onerous calculations - these calculations are automated by this
    package.
	"""
	
	cran = "triangulation" 

	version("0.5.0", md5="c94c0c9ea32d3f174e6aef5855bf9649")

