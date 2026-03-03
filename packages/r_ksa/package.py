# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKsa(RPackage):
	"""Retained Component Criterion for Principal Component Analysis

	The Retained Component Criterion for Principal Component Analysis (RCC_PCA) is a tool to determine the optimal number of components to retain in PCA.
	"""
	
	cran = "KSA" 

	version("0.1.0", md5="473e3985a38a54e67f349dec8af4c42f")

