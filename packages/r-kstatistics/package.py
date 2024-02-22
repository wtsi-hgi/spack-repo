# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKstatistics(RPackage):
	"""Unbiased Estimators for Cumulant Products and Faa Di Bruno's
Formula

	Tools for estimate (joint) cumulants and (joint) products of cumulants of a random sample using (multivariate) k-statistics and (multivariate) polykays, unbiased estimators with minimum variance. Tools for generating univariate and multivariate Faa di Bruno's formula and related polynomials, such as Bell polynomials, generalized complete Bell polynomials, partition polynomials and generalized partition polynomials. For more details see Di Nardo E., Guarino G., Senato D. (2009) <arXiv:0807.5008>, <arXiv:1012.6008>.
	"""
	
	cran = "kStatistics" 

	version("2.1.1", md5="37496a5f5b6aa734971618635d4f6696")

