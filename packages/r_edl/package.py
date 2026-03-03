# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdl(RPackage):
	"""Toolbox for Error-Driven Learning Simulations with Two-Layer
Networks

	Error-driven learning (based on the Widrow & Hoff (1960)<https://isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf> learning rule, and essentially the same as Rescorla-Wagner's learning equations (Rescorla & Wagner, 1972, ISBN: 0390718017), which are also at the core of Naive Discrimination Learning, (Baayen et al, 2011, <doi:10.1037/a0023851>) can be used to explain bottom-up human learning (Hoppe et al, <doi:10.31234/osf.io/py5kd>), but is also at the core of artificial neural networks applications in the form of the Delta rule. This package provides a set of functions for building small-scale simulations to investigate the dynamics of error-driven learning and it's interaction with the structure of the input. For modeling error-driven learning using the Rescorla-Wagner equations the package 'ndl' (Baayen et al, 2011, <doi:10.1037/a0023851>) is available on CRAN at <https://cran.r-project.org/package=ndl>. However, the package currently only allows tracing of a cue-outcome combination, rather than returning the learned networks. To fill this gap, we implemented a new package with a few functions that facilitate inspection of the networks for small error driven learning simulations. Note that our functions are not optimized for training large data sets (no parallel processing), as they are intended for small scale simulations and course examples. (Consider the python implementation 'pyndl' <https://pyndl.readthedocs.io/en/latest/> for that purpose.) 
	"""
	
	cran = "edl" 

	version("1.1", md5="62d78b69ff333417717a2d511e97f1d9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-plotfunctions@1.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
