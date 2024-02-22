# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMthapower(RPackage):
	"""Sample Size and Power for Association Studies Involving
Mitochondrial DNA Haplogroups

	Calculate Sample Size and Power for
    Association Studies Involving Mitochondrial DNA Haplogroups.
    Based on formulae by Samuels et al. AJHG, 2006. 78(4):713-720. <DOI:10.1086/502682>.
	"""
	
	homepage = "https://github.com/aurora-mareviv/mthapower"
	cran = "mthapower" 

	version("0.1.1", md5="567be33d6c5edd677c88e5223617ff2c")

