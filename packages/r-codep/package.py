# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodep(RPackage):
	"""Multiscale Codependence Analysis

	Computation of Multiscale Codependence Analysis and spatial eigenvector maps, as an additional feature.
	"""
	
	cran = "codep" 

	version("0.9-1", md5="4a0ecaa39bc3f7792d32b4360e4e9fab")

	depends_on("r@3:", type=("build", "run"))
