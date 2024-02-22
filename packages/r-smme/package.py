# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmme(RPackage):
	"""Soft Maximin Estimation for Large Scale Heterogeneous Data

	Efficient procedure for solving the soft maximin problem for large scale heterogeneous data, see Lund, Mogensen and Hansen (2022) <doi:10.1111/sjos.12580>. Currently Lasso and SCAD penalized estimation is implemented. Note this package subsumes and replaces the SMMA package.
	"""
	
	cran = "SMME" 

	version("1.1.1", md5="60db0d4b0aa83869371cea44b6ff938f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
