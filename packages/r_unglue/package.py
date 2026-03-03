# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnglue(RPackage):
	"""Extract Matched Substrings Using a Pattern

	Use syntax inspired by the package 'glue' to extract matched substrings in a more intuitive and compact way than by using standard regular expressions.
	"""
	
	cran = "unglue" 

	version("0.1.0", md5="e0928b9e1fa7addcf454896a9e6fbd11")

	depends_on("r@3.1:", type=("build", "run"))
