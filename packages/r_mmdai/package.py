# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmdai(RPackage):
	"""Multivariate Multinomial Distribution Approximation and
Imputation for Incomplete Categorical Data

	A method to impute the missingness in categorical data. Details see the paper <doi:10.4310/SII.2020.v13.n1.a2>.
	"""
	
	cran = "MMDai" 

	version("2.0.0", md5="a29fac5dc3f62ed3937d3ebec178e1a4")

