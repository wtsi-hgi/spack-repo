# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdinterval(RPackage):
	"""Highest (Posterior) Density Intervals

	A generic function and a set of methods to calculate highest density intervals for a variety of classes of objects which can specify a probability density distribution, including MCMC output, fitted density objects, and functions.
	"""
	
	cran = "HDInterval" 

	version("0.2.4", md5="20e8122b31cc3c110d4a65ce4343ef8a")

