# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmt(RPackage):
	"""Estimation of the Rasch Model for Multistage Tests

	Provides conditional maximum likelihood (CML) item parameter estimation of sequential as well as cumulative deterministic multistage designs (Zwitser & Maris, 2015, <doi:10.1007/s11336-013-9369-6>) as well as probabilistic sequential and cumulative multistage designs (Steinfeld & Robitzsch, 2021, <doi:10.31234/osf.io/ew27f>). Supports CML item parameter estimation of conventional linear designs and additional functions for the likelihood ratio test (Andersen, 1973, <doi:10.1007/BF02291180>) as well as functions for the simulation of several kinds of multistage designs. 
	"""
	
	homepage = "https://jansteinfeld.github.io/tmt/"
	cran = "tmt" 

	version("0.3.1-10", md5="11b77ef107c07d0d8d3a8e8fb5acb611")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
