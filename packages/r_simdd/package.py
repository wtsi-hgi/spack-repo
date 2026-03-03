# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimdd(RPackage):
	"""Simulation of Fisher Bingham and Related Directional
Distributions

	Simulation methods for the Fisher Bingham distribution on the unit sphere, the matrix Bingham distribution on a Grassmann manifold, the matrix Fisher distribution on SO(3), and the bivariate von Mises sine model on the torus.
 The methods use an acceptance/rejection simulation algorithm for the Bingham distribution and are described fully by Kent, Ganeiber and Mardia (2018) <doi:10.1080/10618600.2017.1390468>.
 These methods supersede earlier MCMC simulation methods and are more general than earlier simulation methods.
 The methods can be slower in specific situations where there are existing non-MCMC simulation methods (see Section 8 of Kent, Ganeiber and Mardia (2018) <doi:10.1080/10618600.2017.1390468> for further details).
	"""
	
	cran = "simdd" 

	version("1.1-2", md5="a6b3a34b224285614e309e99c22b96c9")

