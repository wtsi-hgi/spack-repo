# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecon(RPackage):
	"""Deconvolution Estimation in Measurement Error Models

	A collection of functions to deal
        with nonparametric measurement error problems using
        deconvolution kernel methods. We focus two measurement error
        models in the package: (1) an additive measurement error model,
        where the goal is to estimate the density or distribution
        function from contaminated data; (2) nonparametric regression
        model with errors-in-variables. The R functions allow the
        measurement errors to be either homoscedastic or
        heteroscedastic. To make the deconvolution estimators
        computationally more efficient in R, we adapt the "Fast Fourier
        Transform" (FFT) algorithm for density estimation with
        error-free data to the deconvolution kernel estimation. Several
        methods for the selection of the data-driven smoothing
        parameter are also provided in the package. See details in:
        Wang, X.F. and Wang, B. (2011). Deconvolution estimation in
        measurement error models: The R package decon. Journal of
        Statistical Software, 39(10), 1-24.
	"""
	
	cran = "decon" 

	version("1.3-4", md5="dc6838ea75fd71c6ba00166780b051b1")

