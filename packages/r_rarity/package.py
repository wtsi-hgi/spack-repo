# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarity(RPackage):
	"""Calculation of Rarity Indices for Species and Assemblages of
Species

	Allows calculation of rarity weights for species and indices of rarity for assemblages of species according to different methods (Leroy et al. 2012, Insect. Conserv. Divers. 5:159-168 <doi:10.1111/j.1752-4598.2011.00148.x>; Leroy et al. 2013, Divers. Distrib. 19:794-803 <doi:10.1111/ddi.12040>). 
	"""
	
	cran = "Rarity" 

	version("1.3-8", md5="cae640452055a28493520c7890abe190")

