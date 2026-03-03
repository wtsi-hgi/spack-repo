# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistances(RPackage):
	"""Tools for Distance Metrics

	Provides tools for constructing, manipulating and using distance metrics.
	"""
	
	homepage = "https://github.com/fsavje/distances"
	cran = "distances" 

	version("0.1.10", md5="35c8224f7b10bc3bc4516294c4ebc440")

	depends_on("r@3.4:", type=("build", "run"))
