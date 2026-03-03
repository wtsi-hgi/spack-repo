# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExact(RPackage):
	"""Unconditional Exact Test

	Performs unconditional exact tests and power calculations for 2x2 contingency tables.
  For comparing two independent proportions, performs Barnard's test (1945)
  <doi:10.1038/156177a0> using the original CSM test (Barnard, 1947 <doi:10.1093/biomet/34.1-2.123>),
  using Fisher's p-value referred to as Boschloo's test (1970) <doi:10.1111/j.1467-9574.1970.tb00104.x>,
  or using a Z-statistic (Suissa and Shuster, 1985, <doi:10.2307/2981892>).
  For comparing two binary proportions, performs unconditional exact test using McNemar's
  Z-statistic (Berger and Sidik, 2003, <doi:10.1191/0962280203sm312ra>),
  using McNemar's conditional p-value, using McNemar's Z-statistic with continuity correction,
  or using CSM test.  Calculates confidence intervals for the difference in proportion.
  This package interacts with pre-computed data available through the ExactData R package,
  which is available in a 'drat' repository.
  Install the ExactData R package from GitHub at <https://pcalhoun1.github.io/drat/>.
  The ExactData R package is approximately 85 MB.
	"""
	
	cran = "Exact" 

	version("3.2", md5="a026b58b9e016ef56f8e07d1a910114c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
