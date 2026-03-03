# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcsmooth(RPackage):
	"""Nonparametric Regression and Bandwidth Selection for Spatial
Models

	Nonparametric smoothing techniques for data on a lattice and
    functional time series. Smoothing is done via kernel regression or
    local polynomial regression, a bandwidth selection procedure based on
    an iterative plug-in algorithm is implemented. This package allows for
    modeling a dependency structure of the error terms of the
    nonparametric regression model.  Methods used in this paper are
    described in Feng/Schaefer (2021)
    <https://ideas.repec.org/p/pdn/ciepap/144.html>, Schaefer/Feng (2021)
    <https://ideas.repec.org/p/pdn/ciepap/143.html>.
	"""
	
	cran = "DCSmooth" 

	version("1.1.2", md5="5a388b1578608ea1863b69bf0035fbda")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
