# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStablelearner(RPackage):
	"""Stability Assessment of Statistical Learning Methods

	Graphical and computational methods that can be used to assess the 
  stability of results from supervised statistical learning.
	"""
	
	cran = "stablelearner" 

	version("0.1-5", md5="130bf063f2caee2991c725ce2c4a8c9a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
