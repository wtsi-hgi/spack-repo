# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPameasures(RPackage):
	"""Prediction and Accuracy Measures for Nonlinear Models and for
Right-Censored Time-to-Event Data

	We propose a pair of summary measures for the predictive power of a prediction
    function based on a regression model. The regression model can be linear
    or nonlinear, parametric, semi-parametric, or nonparametric, and correctly
    specified or mis-specified. The first measure, R-squared, is an extension of
    the classical R-squared statistic for a linear model, quantifying the prediction
    function's ability to capture the variability of the response. The second
    measure, L-squared, quantifies the prediction function's bias for predicting the
    mean regression function. When used together, they give a complete summary of
    the predictive power of a prediction function. Please refer to Gang Li and Xiaoyan Wang (2016) <arXiv:1611.03063> for more details.
	"""
	
	cran = "PAmeasures" 

	version("0.1.0", md5="0e7645163485209acee2187331d7f95a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
