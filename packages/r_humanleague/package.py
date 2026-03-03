# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanleague(RPackage):
	"""Synthetic Population Generator

	Generates high-entropy integer synthetic populations from marginal and (optionally) seed data using quasirandom sampling,
  in arbitrary dimensionality (Smith, Lovelace and Birkin (2017) <doi:10.18564/jasss.3550>).
  The package also provides an implementation of the Iterative Proportional Fitting (IPF) algorithm (Zaloznik (2011) <doi:10.13140/2.1.2480.9923>).
	"""
	
	cran = "humanleague" 

	version("2.3.1", md5="f9733898be8a39815499f3bf4083f884")
	version("2.2.0", md5="429b5e128f567834fce2866f32598eb0")

	depends_on("r-rcpp", type=("build", "run"))
