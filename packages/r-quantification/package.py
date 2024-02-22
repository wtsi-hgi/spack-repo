# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantification(RPackage):
	"""Quantification of Qualitative Survey Data

	Provides different functions for quantifying qualitative survey data. It supports the Carlson-Parkin method, the regression approach, the balance approach and the conditional expectations method.
	"""
	
	cran = "quantification" 

	version("0.2.0", md5="e65adea337af3623a921c309312fd49c")

	depends_on("r-car", type=("build", "run"))
