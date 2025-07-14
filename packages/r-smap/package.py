# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmap(RPackage):
	"""A Segmental Maximum A Posteriori Approach to Array-CGH Copy Number Profiling

	Functions and classes for DNA copy number profiling of array-CGH data
	"""
	
	bioc = "SMAP"

	version("1.66.0", commit="1ecee675bf4432ff11b909bd2b112fe28984aaf3")

	depends_on("r@2.10:", type=("build", "run"))
