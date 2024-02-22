# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRai(RPackage):
	"""Revisiting-Alpha-Investing for Polynomial Regression

	A modified implementation of stepwise regression that greedily searches 
    the space of interactions among features in order to build polynomial regression models.
    Furthermore, the hypothesis tests conducted are valid-post model selection
    due to the use of a revisiting procedure that implements an alpha-investing
    rule. As a result, the set of rejected sequential hypotheses is proven to 
    control the marginal false discover rate. When not searching for polynomials,
    the package provides a statistically valid algorithm
    to run and terminate stepwise regression. For more information, see 
    Johnson, Stine, and Foster (2019) <arXiv:1510.06322>.
	"""
	
	homepage = "https://github.com/korydjohnson/rai"
	cran = "rai" 

	version("1.0.0", md5="a766cd3baa87c7b2803d47b889142ec3")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
