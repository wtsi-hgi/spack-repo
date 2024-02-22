# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlfsm(RPackage):
	"""Simulations and Statistical Inference for Linear Fractional
Stable Motions

	Contains functions for simulating the linear fractional stable motion according to the algorithm developed by Mazur and Otryakhin <doi:10.32614/RJ-2020-008> based on the method from Stoev and Taqqu (2004) <doi:10.1142/S0218348X04002379>, as well as functions for estimation of parameters of these processes introduced by Mazur, Otryakhin and Podolskij (2018) <arXiv:1802.06373>, and also different related quantities.
	"""
	
	homepage = "https://gitlab.com/Dmitry_Otryakhin/Tools-for-parameter-estimation-of-the-linear-fractional-stable-motion"
	cran = "rlfsm" 

	version("1.1.2", md5="35394d708c6d57ab2d8d00a437a680ea")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stabledist", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
