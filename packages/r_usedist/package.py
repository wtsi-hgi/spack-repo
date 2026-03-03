# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsedist(RPackage):
	"""Distance Matrix Utilities

	Functions to re-arrange, extract, and work with distances.
	"""
	
	cran = "usedist" 

	version("0.4.0", md5="1c47103a94b8a1f69029c06457328681")

