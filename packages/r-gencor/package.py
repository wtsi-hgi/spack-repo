# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGencor(RPackage):
	"""Generate Customized Correlation Matrices

	Provides a function that generates a customized correlation matrix based on limit values and proportions for intervals composed by its limits. It can also generate random matrices with low, medium, and high correlations, in which low, medium, and high thresholds are user-defined.
	"""
	
	cran = "gencor" 

	version("1.0.2", md5="b4e9d26976f85f0b4f0f1e65c9845193")

