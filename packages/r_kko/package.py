# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKko(RPackage):
	"""Kernel Knockoffs Selection for Nonparametric Additive Models

	A variable selection procedure, dubbed KKO, for nonparametric additive model with finite-sample false discovery rate control guarantee. The method integrates three key components: knockoffs, subsampling for stability, and random feature mapping for nonparametric function approximation. For more information, see the accompanying paper: Dai, X., Lyu, X., & Li, L. (2021). “Kernel Knockoffs Selection for Nonparametric Additive Models”. arXiv preprint <arXiv:2105.11659>.
	"""
	
	cran = "kko" 

	version("1.0.1", md5="cb06bff76fd64888d09b80ceb3e03abb")

	depends_on("r@3.6.3:", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
	depends_on("r-knockoff", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-extdist", type=("build", "run"))
