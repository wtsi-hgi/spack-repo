# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesorddesign(RPackage):
	"""Bayesian Group Sequential Design for Ordinal Data

	The proposed group-sequential trial design is based on Bayesian methods for ordinal endpoints, 
             including three methods, the proportional-odds-model (PO)-based, non-proportional-odds-model (NPO)-based, 
             and PO/NPO switch-model-based designs, which makes our proposed methods generic to be able to deal with 
             various scenarios.
             Richard J. Barker, William A. Link (2013) <doi:10.1080/00031305.2013.791644>.
             Thomas A. Murray, Ying Yuan, Peter F. Thall, Joan H. Elizondo, Wayne L.Hofstetter (2018) <doi:10.1111/biom.12842>.
             Chengxue Zhong, Haitao Pan, Hongyu Miao (2021) <arXiv:2108.06568>.
	"""
	
	cran = "BayesOrdDesign" 

	version("0.1.2", md5="a261504145d054dc52eabd1c240d0a69")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-schoolmath", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-gsdesign", type=("build", "run"))
	depends_on("r-superdiag", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-madness", type=("build", "run"))
	depends_on("r-rjmcmc", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
