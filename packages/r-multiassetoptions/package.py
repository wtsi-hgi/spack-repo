# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiassetoptions(RPackage):
	"""Finite Difference Method for Multi-Asset Option Valuation

	Efficient finite difference method for valuing European and American multi-asset options.
	"""
	
	cran = "multiAssetOptions" 

	version("0.1-2", md5="4d710dc840c00c1927a7cd7a9223a166")

	depends_on("r-matrix", type=("build", "run"))
