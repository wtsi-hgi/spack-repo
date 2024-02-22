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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SMAP_1.66.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SMAP/SMAP_1.66.0.tar.gz"]

	version("1.66.0", md5="f29ffdead8f34c2f531dd7ea764febe0")

	depends_on("r@2.10:", type=("build", "run"))
