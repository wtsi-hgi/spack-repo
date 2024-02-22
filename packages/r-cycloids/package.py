# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCycloids(RPackage):
	"""Tools for Calculating Hypocycloids, Epicycloids, Hypotrochoids,
and Epitrochoids

	Tools for calculating coordinate representations of
    hypocycloids, epicyloids, hypotrochoids, and epitrochoids
    (altogether called 'cycloids' here) with different scaling
    and positioning options. The cycloids can be visualised with
    any appropriate graphics function in R.
	"""
	
	cran = "cycloids" 

	version("1.0.2", md5="61bdfd2937e8fefd8e0f85b5b981d16f")

