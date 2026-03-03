# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegress(RPackage):
	"""Gaussian Linear Models with Linear Covariance Structure

	Functions to fit Gaussian linear model by maximising the
        residual log likelihood where the covariance structure can be
        written as a linear combination of known matrices.  Can be used
        for multivariate models and random effects models.  Easy
        straight forward manner to specify random effects models,
        including random interactions. Code now optimised to use
        Sherman Morrison Woodbury identities for matrix inversion in
        random effects models. We've added the ability to fit models
        using any kernel as well as a function to return the mean and
        covariance of random effects conditional on the data (best
        linear unbiased predictors, BLUPs).
        Clifford and McCullagh (2006)
        <https://www.r-project.org/doc/Rnews/Rnews_2006-2.pdf>.
	"""
	
	homepage = "https://github.com/kbroman/regress"
	cran = "regress" 

	version("1.3-21", md5="b460e3107c80b61e4ebad5a8665fdae8")

