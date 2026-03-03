# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnotr(RPackage):
	"""Knot Diagrams using Bezier Curves

	Makes visually pleasing diagrams of knot projections using optimized Bezier curves.
	"""
	
	cran = "knotR" 

	version("1.0-4", md5="445228f9888fb8ec5b8e42a9ae3c65a1")

	depends_on("r@2.10:", type=("build", "run"))
