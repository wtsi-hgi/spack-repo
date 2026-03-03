# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRleafangle(RPackage):
	"""Estimates, Plots and Evaluates Leaf Angle Distribution
Functions, Calculates Extinction Coefficients

	Leaf angle distribution is described by a number of functions
    (e.g. ellipsoidal, Beta and rotated ellipsoidal). The parameters of leaf angle
    distributions functions are estimated through different empirical relationship.
    This package includes estimations of parameters of different leaf angle
    distribution function, plots and evaluates leaf angle distribution functions,
    calculates extinction coefficients given leaf angle distribution.
    Reference: Wang(2007)<doi:10.1016/j.agrformet.2006.12.003>. 
	"""
	
	cran = "RLeafAngle" 

	version("1.0", md5="f35a499eafe696fcbd81898a25e0f367")

