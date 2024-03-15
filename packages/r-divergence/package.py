# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDivergence(RPackage):
	"""Divergence: Functionality for assessing omics data by divergence with respect to a baseline

	This package provides functionality for performing divergence analysis as presented in Dinalankara et al, "Digitizing omics profiles by divergence from a baseline", PANS 2018. This allows the user to simplify high dimensional omics data into a binary or ternary format which encapsulates how the data is divergent from a specified baseline group with the same univariate or multivariate features.
	"""
	
	bioc = "divergence" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/divergence_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/divergence/divergence_1.18.0.tar.gz"]

	version("1.18.0", md5="0ead0047c69549361f0f86d7207aee2b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
