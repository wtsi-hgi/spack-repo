# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCubicbsplines(RPackage):
	"""Computation of a Cubic B-Spline Basis and Its Derivatives

	Computation of a cubic B-spline basis for arbitrary knots. It also provides the 1st and 2nd derivatives, as well as the integral of the basis elements. It is used by the author to fit penalized B-spline models, see e.g. Jullion, A. and Lambert, P. (2006) <doi:10.1016/j.csda.2006.09.027>,  Lambert, P. and  Eilers, P.H.C. (2009) <doi:10.1016/j.csda.2008.11.022> and, more recently, Lambert, P. (2021) <doi:10.1016/j.csda.2021.107250>. It is inspired by the algorithm developed by de Boor, C. (1977) <doi:10.1137/0714026>.
	"""
	
	homepage = "http://www.statsoc.ulg.ac.be/"
	cran = "cubicBsplines" 

	version("1.0.0", md5="b4c35158e221619d50d06bc8e63c3af5")

