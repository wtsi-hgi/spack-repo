# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatastepr(RPackage):
	"""An Implementation of a SAS-Style Data Step

	Based on a SAS data step. This allows for row-wise dynamic building
    of data, iteratively importing slices of existing dataframes, conducting
    analyses, and exporting to a results frame. This is particularly useful for
    differential or time-series analyses, which are often not well suited to vector-
    based operations.
	"""
	
	homepage = "https://github.com/bramtayl/datastepr"
	cran = "datastepr" 

	version("0.0.2", md5="3649d6d318c9967b6154230add1d99e8")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-lazyeval@0.1.10:", type=("build", "run"))
	depends_on("r-r6@2.0.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tibble@1.1:", type=("build", "run"))
