# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisclap(RPackage):
	"""Discrete Laplace Exponential Family

	The discrete Laplace exponential family for use in fitting generalized linear models.
	"""
	
	cran = "disclap" 

	version("1.5.1", md5="d710cbc8affa55c36c4fdbb000d16f97")

