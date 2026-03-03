# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDivdyn(RPackage):
	"""Diversity Dynamics using Fossil Sampling Data

	Functions to describe sampling and diversity dynamics of fossil occurrence datasets (e.g. from the Paleobiology Database). The package includes methods to calculate range- and occurrence-based metrics of taxonomic richness, extinction and origination rates, along with traditional sampling measures. A powerful subsampling tool is also included that implements frequently used sampling standardization methods in a multiple bin-framework. The plotting of time series and the occurrence data can be simplified by the functions incorporated in the package, as well as other calculations, such as environmental affinities and extinction selectivity testing. Details can be found in: Kocsis, A.T.; Reddin, C.J.; Alroy, J. and Kiessling, W. (2019) <doi:10.1101/423780>.
	"""
	
	cran = "divDyn" 

	version("0.8.2", md5="96403380a609208379e1ae2c0183fba5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
