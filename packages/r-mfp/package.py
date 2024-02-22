# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfp(RPackage):
	"""Multivariable Fractional Polynomials

	Fractional polynomials are used to represent curvature in regression models. A key reference is Royston and Altman, 1994.
	"""
	
	cran = "mfp" 

	version("1.5.4", md5="63890352762021f831f0d9b00204fbcd")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
