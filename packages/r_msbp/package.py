# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbp(RPackage):
	"""Multiscale Bernstein Polynomials for Densities

	Performs Bayesian nonparametric multiscale density estimation and multiscale testing of group differences with multiscale Bernstein polynomials (msBP) mixtures as in Canale and Dunson (2016).
	"""
	
	cran = "msBP" 

	version("1.4-1", md5="af92cd09faa8f45871d46471de7535cc")

