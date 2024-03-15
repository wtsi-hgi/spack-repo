# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymts(RPackage):
	"""Symmetric Tempered Stable Distributions

	Contains methods for simulation and for evaluating the pdf, cdf, and quantile functions for symmetric stable, symmetric classical tempered stable, and symmetric power tempered stable distributions. 
	"""
	
	cran = "SymTS" 

	version("1.0-2", md5="9b0d43c8702bdd351f392245c45abbfe")

