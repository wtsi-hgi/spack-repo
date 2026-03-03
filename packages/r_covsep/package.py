# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovsep(RPackage):
	"""Tests for Determining if the Covariance Structure of
2-Dimensional Data is Separable

	Functions for testing if the covariance structure of 2-dimensional data
    (e.g. samples of surfaces X_i = X_i(s,t)) is separable, i.e. if covariance(X) =
    C_1 x C_2.
    A complete descriptions of the implemented tests can be found in the paper
    Aston, John A. D.; Pigoli, Davide; Tavakoli, Shahin. Tests for separability in
    nonparametric covariance operators of random surfaces. Ann. Statist. 45 (2017),
    no. 4, 1431--1461. <doi:10.1214/16-AOS1495> <https://projecteuclid.org/euclid.aos/1498636862> <arXiv:1505.02023>.
	"""
	
	homepage = "http://arxiv.org/abs/1505.02023"
	cran = "covsep" 

	version("1.1.0", md5="7bd69305cfeee78aa91079572f39bf3d")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.4:", type=("build", "run"))
