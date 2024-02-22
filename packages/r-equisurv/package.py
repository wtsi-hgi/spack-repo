# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquisurv(RPackage):
	"""Modeling, Confidence Intervals and Equivalence of Survival
Curves

	We provide a non-parametric and a parametric approach to investigate the equivalence (or non-inferiority) of two survival curves, obtained from two given datasets. The test is based on the creation of confidence intervals at pre-specified time points.
    For the non-parametric approach, the curves are given by Kaplan-Meier curves and the variance for calculating the confidence intervals is obtained by Greenwood's formula.
    The parametric approach is based on estimating the underlying distribution, where the user can choose between a Weibull, Exponential, Gaussian, Logistic, Log-normal or a Log-logistic distribution. Estimates for the variance for calculating the confidence bands are obtained by a (parametric) bootstrap approach. For this bootstrap censoring is assumed to be exponentially distributed and estimates are obtained from the datasets under consideration.
    All details can be found in K.Moellenhoff and A.Tresch: Survival analysis under non-proportional hazards: investigating non-inferiority or equivalence in time-to-event data <arXiv:2009.06699>.
	"""
	
	cran = "EquiSurv" 

	version("0.1.0", md5="f61d25261a53f7863b1ec382c22f6217")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-eha", type=("build", "run"))
