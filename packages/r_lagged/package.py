# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLagged(RPackage):
	"""Classes and Methods for Lagged Objects

	Provides classes and methods for objects, whose indexing
      naturally starts from zero. Subsetting, indexing and mathematical
      operations are defined naturally between lagged objects and lagged
      and base R objects. Recycling is not used, except for singletons.
      The single bracket operator doesn't drop dimensions by default.
	"""
	
	homepage = "https://github.com/GeoBosh/lagged"
	cran = "lagged" 

	version("0.3.2", md5="92fe0d5243e9159639d690a427d6dbc7")

