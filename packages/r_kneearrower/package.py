# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKneearrower(RPackage):
	"""Finds Cutoff Points on Knee Curves

	Given a set of points around a knee curve,
    analyzes first and second derivatives to find knee points.
	"""
	
	cran = "KneeArrower" 

	version("1.0.0", md5="84ec78afad3c74bc4c007baea1721365")

	depends_on("r-signal", type=("build", "run"))
