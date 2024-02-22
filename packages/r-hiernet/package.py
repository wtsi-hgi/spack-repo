# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiernet(RPackage):
	"""A Lasso for Hierarchical Interactions

	Fits sparse interaction models for continuous and binary responses subject to the strong (or weak) hierarchy restriction that an interaction between two variables only be included if both (or at least one of) the variables is included as a main effect.  For more details, see Bien, J., Taylor, J., Tibshirani, R., (2013) "A Lasso for Hierarchical Interactions." Annals of Statistics. 41(3). 1111-1141.
	"""
	
	cran = "hierNet" 

	version("1.9", md5="b7283e609a7b6f280241c681d32a22bd")

