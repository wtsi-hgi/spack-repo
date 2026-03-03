# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdar(RPackage):
	"""Discriminant Analysis Incorporating Individual Uncertainties

	The qda() function from package 'MASS' is extended to calculate a weighted linear (LDA) and quadratic discriminant analysis (QDA) by changing the group variances and group means based on cell-wise uncertainties.
    The uncertainties can be derived e.g. through relative errors for each individual measurement (cell), not only row-wise or column-wise uncertainties.
    The method can be applied compositional data (e.g. portions of substances, concentrations) and non-compositional data.
	"""
	
	cran = "vdar" 

	version("0.1.3-2", md5="80259b4389860b829fd90df08a99875f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
