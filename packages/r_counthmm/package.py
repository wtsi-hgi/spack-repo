# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCounthmm(RPackage):
	"""Penalized Estimation of Flexible Hidden Markov Models for Time
Series of Counts

	Provides tools for penalized estimation of flexible hidden Markov models for time series of counts w/o the need to specify a (parametric) family of distributions. These include functions for model fitting, model checking, and state decoding. For details, see Adam, T., Langrock, R., and Weiß, C.H. (2019): Penalized Estimation of Flexible Hidden Markov Models for Time Series of Counts. <arXiv:1901.03275>.
	"""
	
	cran = "countHMM" 

	version("0.1.0", md5="4f56ef699d7dcdebbc95a3863b295d75")

