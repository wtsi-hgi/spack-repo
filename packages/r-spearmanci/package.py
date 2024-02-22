# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpearmanci(RPackage):
	"""Jackknife Euclidean / Empirical Likelihood Inference for
Spearman's Rho

	Functions for conducting jackknife Euclidean / empirical likelihood inference for Spearman's rho (de Carvalho and Marques (2012) <10.1080/10920277.2012.10597644>).
	"""
	
	cran = "spearmanCI" 

	version("1.0", md5="5467e2f7460fa5302cd13b7ad09bf1e6")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-emplik", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
