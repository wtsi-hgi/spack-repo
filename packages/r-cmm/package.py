# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmm(RPackage):
	"""Categorical Marginal Models

	Quite extensive package for maximum likelihood estimation and
    weighted least squares estimation of categorical marginal models (CMMs;
    e.g., Bergsma and Rudas, 2002, <http://www.jstor.org/stable/2700006?;
    Bergsma, Croon and Hagenaars, 2009, <DOI:10.1007/b12532>.
	"""
	
	cran = "cmm" 

	version("1.0", md5="be1d038d3925d7dfdec32e45330922e2")

