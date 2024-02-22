# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfilmm(RPackage):
	"""Generalized Fiducial Inference for Normal Linear Mixed Models

	Simulation of the generalized fiducial distribution for
    normal linear mixed models with interval data. Fiducial inference is
    somehow similar to Bayesian inference, in the sense that it is based
    on a distribution that represents the uncertainty about the
    parameters, like the posterior distribution in Bayesian statistics. It
    does not require a prior distribution, and it yields results close to
    frequentist results. Reference: Cisewski and Hannig (2012)
    <doi:10.1214/12-AOS1030>.
	"""
	
	homepage = "https://github.com/stla/gfilmm"
	cran = "gfilmm" 

	version("2.0.5", md5="a893fd5014db30c05be7d230bec996ba")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-spatstat@2:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
