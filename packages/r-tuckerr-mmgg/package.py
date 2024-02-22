# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTuckerrMmgg(RPackage):
	"""Three-Mode Principal Components Analysis

	Performs Three-Mode Principal Components Analysis,
    which carries out Tucker Models.
	"""
	
	homepage = "https://github.com/gusart/tuckerR_mmgg"
	cran = "tuckerR.mmgg" 

	version("1.5.1", md5="d29a9bb293134b3ee7a2fcb749af39fa")

	depends_on("r@3.3:", type=("build", "run"))
