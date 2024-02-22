# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuickblock(RPackage):
	"""Quick Threshold Blocking

	
    Provides functions for assigning treatments in randomized experiments using
    near-optimal threshold blocking. The package is made with large data sets in
    mind and derives blocks more than an order of magnitude quicker than other
    methods.
	"""
	
	homepage = "https://github.com/fsavje/quickblock"
	cran = "quickblock" 

	version("0.2.1", md5="847a76e6a049ad7a846ba251a76cf84c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distances", type=("build", "run"))
	depends_on("r-scclust@0.2:", type=("build", "run"))
