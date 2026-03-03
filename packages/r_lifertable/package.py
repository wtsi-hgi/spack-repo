# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifertable(RPackage):
	"""Life and Fertility Tables Specially for Insects

	Life and Fertility Tables are appropriate to study the dynamics of 
    arthropods populations. This package provides utilities for constructing
    Life Tables and Fertility Tables, related demographic parameters, and some
    simple graphs of interest. It also offers functions to transform the
    obtained data into a known format for better manipulation. This document is
    based on the article by Maia, Luiz, and Campanhola "Statistical Inference on
    Associated Fertility Life Table Parameters Using Jackknife Technique
    Computational Aspects" (April 2000, Journal of Economic Entomology, Volume
    93, Issue 2) <doi:10.1603/0022-0493-93.2.511>.
	"""
	
	cran = "Lifertable" 

	version("0.0.1", md5="016dd625e3bda303009dd3e12e0eeacf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
