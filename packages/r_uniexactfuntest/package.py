# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniexactfuntest(RPackage):
	"""Uniform Exact Functional Tests for Contingency Tables

	Testing whether two discrete variables have a functional
  relationship under null distributions where the two variables are
  statistically independent with fixed marginal counts.
  The fast enumeration algorithm was based on (Nguyen et al. 2020) <doi:10.24963/ijcai.2020/372>.
	"""
	
	cran = "UniExactFunTest" 

	version("1.0.0", md5="1ff914084ebd368ea677c6434c4e5d08")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
