# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmdu(RPackage):
	"""(Restricted) [external] Multidimensional Unfolding

	Functions for performing (external) multidimensional unfolding.
             Restrictions (fixed coordinates or model restrictions) are available for both row and column coordinates in all combinations.
	"""
	
	cran = "fmdu" 

	version("0.1.1", md5="c859e67c12b8f2d31b9e50b9b9231624")
	version("0.1.0", md5="ea5d0b9359bab857fd42ca17d4a1a503")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
