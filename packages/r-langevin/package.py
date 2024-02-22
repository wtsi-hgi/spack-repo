# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLangevin(RPackage):
	"""Langevin Analysis in One and Two Dimensions

	Estimate drift and diffusion functions from time series and
    generate synthetic time series from given drift and diffusion coefficients.
	"""
	
	homepage = "https://gitlab.uni-oldenburg.de/TWiSt/Langevin"
	cran = "Langevin" 

	version("1.3.1", md5="bc491495086d3c9d1c6475b3f06f2608")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.4.600:", type=("build", "run"))
