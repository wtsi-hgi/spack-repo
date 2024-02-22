# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynr(RPackage):
	"""Dynamic Models with Regime-Switching

	Intensive longitudinal data have become increasingly prevalent in
    various scientific disciplines. Many such data sets are noisy, multivariate,
    and multi-subject in nature. The change functions may also be continuous,
    or continuous but interspersed with periods of discontinuities (i.e.,
    showing regime switches). The package 'dynr' (Dynamic Modeling in R) is an
    R package that implements a set of computationally efficient algorithms for
    handling a broad class of linear and nonlinear discrete- and continuous-time
    models with regime-switching properties under the constraint of linear
    Gaussian measurement functions. The discrete-time models can generally
    take on the form of a state-space or difference equation model. The
    continuous-time models are generally expressed as a set of ordinary or
    stochastic differential equations. All estimation and computations are
    performed in C, but users are provided with the option to specify the
    model of interest via a set of simple and easy-to-learn model specification
    functions in R. Model fitting can be performed using single-subject time
    series data or multiple-subject longitudinal data. Ou, Hunter, & Chow
    (2019) <doi:10.32614%2FRJ-2019-012> provided a detailed introduction to the
    interface and more information on the algorithms.
	"""
	
	homepage = "https://dynrr.github.io/"
	cran = "dynr" 

	version("0.1.16-105", md5="94cd1977dde6499b4c68fb310ec35f2a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
