# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForeco(RPackage):
	"""Forecast Reconciliation

	Classical (bottom-up and top-down), optimal and heuristic combination forecast 
    point (Di Fonzo and Girolimetto, 2023) <doi:10.1016/j.ijforecast.2021.08.004> and 
    probabilistic (Girolimetto et al. 2023) <arXiv:2303.17277> reconciliation procedures 
    for cross-sectional, temporal, and cross-temporal linearly constrained time series.
	"""
	
	homepage = "https://github.com/daniGiro/FoReco"
	cran = "FoReco" 

	version("0.2.6", md5="869117c61ab725bb37c9ff9d382c85cb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
