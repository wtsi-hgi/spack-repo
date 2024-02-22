# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmr(RPackage):
	"""Externally Studentized Midrange Distribution

	Computes the studentized midrange distribution (pdf, cdf and quantile) and generates random numbers.
	"""
	
	homepage = "https://bendeivide.github.io/SMR/"
	cran = "SMR" 

	version("2.1.0", md5="44c60bafd4d9996f4becb1768b143b38")

	depends_on("r-rcpp", type=("build", "run"))
