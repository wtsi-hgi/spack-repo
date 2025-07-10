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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SMAP_1.66.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SMAP/SMAP_1.66.0.tar.gz"]

	version("1.66.0", sha256="b68c532cdbffdde5789ebd823eaceda95ae3d4d041e687363363da2bc7dad254")

	depends_on("r@2.10:", type=("build", "run"))
