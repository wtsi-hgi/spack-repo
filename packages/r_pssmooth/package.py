# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPssmooth(RPackage):
	"""Flexible and Efficient Evaluation of Principal
Surrogates/Treatment Effect Modifiers

	Implements estimation and testing procedures for evaluating an intermediate biomarker response as a principal surrogate of a clinical response to treatment (i.e., principal stratification effect modification analysis), as described in Juraska M, Huang Y, and Gilbert PB (2020), Inference on treatment effect modification by biomarker response in a three-phase sampling design, Biostatistics, 21(3): 545-560 <doi:10.1093/biostatistics/kxy074>. The methods avoid the restrictive 'placebo structural risk' modeling assumption common to past methods and further improve robustness by the use of nonparametric kernel smoothing for biomarker density estimation. A randomized controlled two-group clinical efficacy trial is assumed with an ordered categorical or continuous univariate biomarker response measured at a fixed timepoint post-randomization and with a univariate baseline surrogate measure allowed to be observed in only a subset of trial participants with an observed biomarker response (see the flexible three-phase sampling design in the paper for details). Bootstrap-based procedures are available for pointwise and simultaneous confidence intervals and testing of four relevant hypotheses. Summary and plotting functions are provided for estimation results.
	"""
	
	homepage = "https://github.com/mjuraska/pssmooth"
	cran = "pssmooth" 

	version("1.0.3", md5="0b6812a7f4b817f7cc3114a2a5ec7750")

	depends_on("r-osdesign", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-chngpt", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
