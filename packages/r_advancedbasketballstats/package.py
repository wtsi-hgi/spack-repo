# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdvancedbasketballstats(RPackage):
	"""Advanced Basketball Statistics

	Provides different functionalities and calculations used in the world of basketball to analyze the statistics of the players, the statistics of the teams, the statistics of the quintets and the statistics of the plays. For more details of the calculations included in the package can be found in the book Basketball on Paper written by Dean Oliver.
	"""
	
	cran = "AdvancedBasketballStats" 

	version("1.0.1", md5="197a134f51aee66da775663e6ce46bd9")

