# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcopula(RPackage):
	"""Modelling Dependence with Multivariate Archimax (or any
User-Defined Continuous) Copulas

	Archimax copulas are mixture of Archimedean and EV copulas. The package provides definitions of several parametric families of generator and dependence function, computes CDF and PDF, estimates parameters, tests for goodness of fit, generates random sample and checks copula properties for custom constructs. In 2-dimensional case explicit formulas for density are used, contrary to higher dimensions when all derivatives are linearly approximated. Several non-archimax families (normal, FGM, Plackett) are provided as well.
	"""
	
	cran = "acopula" 

	version("0.9.4", md5="912c850bcba7e3960cf46764467bf0ef")

