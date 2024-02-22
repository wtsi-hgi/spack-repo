# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlm(RPackage):
	"""Bayesian and Likelihood Analysis of Dynamic Linear Models

	Provides routines for Maximum likelihood,
    Kalman filtering and smoothing, and Bayesian
    analysis of Normal linear State Space models, also known as 
    Dynamic Linear Models. 
	"""
	
	cran = "dlm" 

	version("1.1-6", md5="e50c3702f6b2b95f1605a4ed1bfb73e6")

