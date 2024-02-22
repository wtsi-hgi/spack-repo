# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBvar(RPackage):
	"""Hierarchical Bayesian Vector Autoregression

	Estimation of hierarchical Bayesian vector autoregressive models
    following Kuschnig & Vashold (2021) <doi:10.18637/jss.v100.i14>.
    Implements hierarchical prior selection for conjugate priors in the fashion
    of Giannone, Lenza & Primiceri (2015) <doi:10.1162/REST_a_00483>.
    Functions to compute and identify impulse responses, calculate forecasts,
    forecast error variance decompositions and scenarios are available.
    Several methods to print, plot and summarise results facilitate analysis.
	"""
	
	homepage = "https://github.com/nk027/bvar"
	cran = "BVAR" 

	version("1.0.5", md5="600d620503dbf681e33aae4203427dd0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
