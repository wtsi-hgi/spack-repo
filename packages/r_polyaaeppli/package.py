# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyaaeppli(RPackage):
	"""Implementation of the Polya-Aeppli Distribution

	Functions for evaluating the mass density, cumulative distribution function, quantile function and random variate generation for the Polya-Aeppli distribution, also known as the geometric compound Poisson distribution.  More information on the implementation can be found at Conrad J. Burden (2014) <arXiv:1406.2780>.
	"""
	
	cran = "polyaAeppli" 

	version("2.0.2", md5="165307369dcdbf69067b034afe13da18")

	depends_on("r@3:", type=("build", "run"))
