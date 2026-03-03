# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcdfht(RPackage):
	"""Empirical CDF for Heavy Tailed Data

	Computes and plots a transformed empirical CDF (ecdf) as a
    diagnostic for heavy tailed data, specifically data with power law decay on the
    tails.  Routines for annotating the plot, comparing data to a model, fitting a
    nonparametric model, and some multivariate extensions are given.
	"""
	
	cran = "ecdfHT" 

	version("0.1.1", md5="fe8af4ba8cd44f712afcb876926504e1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
