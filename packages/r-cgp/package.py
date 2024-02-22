# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgp(RPackage):
	"""Composite Gaussian Process Models

	Fit composite Gaussian process (CGP) models as described in Ba and Joseph (2012) "Composite Gaussian Process Models for Emulating Expensive Functions", Annals of Applied Statistics. The CGP model is capable of approximating complex surfaces that are not second-order stationary.  Important functions in this package are CGP, print.CGP, summary.CGP, predict.CGP and plotCGP.
	"""
	
	cran = "CGP" 

	version("2.1-1", md5="a787a92b4d1dc512a33e5dd39d76e8af")

