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

	version("1.24.0", commit="6b0d5ab407ce4f82db84a46cd4841766086353c1")
	version("1.18.0", commit="7ec43c9ca3a681044eb9eeca449d2c6f13fe2d5a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
