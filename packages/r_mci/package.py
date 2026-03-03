# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMci(RPackage):
	"""Multiplicative Competitive Interaction (MCI) Model

	Market area models are used to analyze and predict store choices and market areas concerning retail and service locations. This package implements two market area models (Huff Model, Multiplicative Competitive Interaction Model) into R, while the emphases lie on 1.) fitting these models based on empirical data via OLS regression and nonlinear techniques and 2.) data preparation and processing (esp. interaction matrices and data preparation for the MCI Model).
	"""
	
	cran = "MCI" 

	version("1.3.3", md5="3ae266e1397e296472ba831f8b7a3355")

