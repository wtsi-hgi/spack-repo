# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpemd(RPackage):
	"""A Bi-Dimensional Implementation of the Empirical Mode
Decomposition for Spatial Data

	This implementation of the Empirical Mode Decomposition (EMD) works in 2 dimensions simultaneously, and 
    can be applied on spatial data. It can handle both gridded or un-gridded datasets.
	"""
	
	homepage = "https://github.com/pierreroudier/spemd"
	cran = "spemd" 

	version("0.1-1", md5="e5a9a2d915575e7449d7fe106144c60c")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
