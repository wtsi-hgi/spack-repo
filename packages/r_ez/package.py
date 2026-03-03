# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REz(RPackage):
	"""Easy Analysis and Visualization of Factorial Experiments

	Facilitates easy analysis of factorial experiments, including
    purely within-Ss designs (a.k.a. "repeated measures"), purely between-Ss
    designs, and mixed within-and-between-Ss designs. The functions in this package
    aim to provide simple, intuitive and consistent specification of data analysis
    and visualization. Visualization functions also include design visualization for
    pre-analysis data auditing, and correlation matrix visualization. Finally, this
    package includes functions for non-parametric analysis, including permutation
    tests and bootstrap resampling. The bootstrap function obtains predictions
    either by cell means or by more advanced/powerful mixed effects models, yielding
    predictions and confidence intervals that may be easily visualized at any level
    of the experiment's design.
	"""
	
	homepage = "http://github.com/mike-lawrence/ez"
	cran = "ez" 

	version("4.4-0", md5="e8568bc9583caa7d934272eeb1e17750")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-car@2.1.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-lme4@1.1.12:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-matrix@1.2.7.1:", type=("build", "run"))
	depends_on("r-mgcv@1.8.12:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-scales@0.4:", type=("build", "run"))
	depends_on("r-stringr@1.1:", type=("build", "run"))
