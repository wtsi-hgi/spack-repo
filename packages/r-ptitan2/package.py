# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtitan2(RPackage):
	"""Permutations of Treatment Labels and TITAN2 Analysis

	Permute treatment labels for taxa and environmental gradients to
    generate an empirical distribution of change points.  This is an extension
    for the 'TITAN2' package <https://cran.r-project.org/package=TITAN2>.
	"""
	
	homepage = "https://github.com/USEPA/pTITAN2"
	cran = "pTITAN2" 

	version("1.0.2", md5="40c439ac70f863858bfe79498a931565", url="https://cran.r-project.org/src/contrib/pTITAN2_1.0.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
