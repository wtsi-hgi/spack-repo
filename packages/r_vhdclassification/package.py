# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVhdclassification(RPackage):
	"""Discrimination/Classification in very high dimension with linear
and quadratic rules

	This package provides an implementation of Linear discriminant analysis and quadratic discriminant analysis that works fine in very high dimension (when there are many more variables than observations). 
	"""
	
	cran = "VHDClassification" 

	version("0.3", md5="4442e697ec0f95c55fe17d586769df62")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
