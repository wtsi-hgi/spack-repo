# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHierinf(RPackage):
	"""Hierarchical Inference

	Tools to perform hierarchical inference for one or multiple studies / data sets based on high-dimensional multivariate (generalised) linear models. A possible application is to perform hierarchical inference for GWA studies to find significant groups or single SNPs (if the signal is strong) in a data-driven and automated procedure. The method is based on an efficient hierarchical multiple testing correction and controls the FWER. The functions can easily be run in parallel.
	"""
	
	bioc = "hierinf"

	version("1.26.0", commit="f83f9ac3486c5d5e9811efeefc53cc1a954a5844")
	version("1.20.0", commit="59979c17ed19eb3be70e3951bfe32c7b06db225c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
