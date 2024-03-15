# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHidimda(RPackage):
	"""High Dimensional Discriminant Analysis

	Performs linear discriminant analysis in high dimensional
        problems based on reliable covariance estimators for problems
        with (many) more variables than observations. Includes routines
        for classifier training, prediction, cross-validation and
        variable selection.
	"""
	
	cran = "HiDimDA" 

	version("0.2-6", md5="e7afadeebd1c5025083ce027827b2844")

	depends_on("r@2.10:", type=("build", "run"))
