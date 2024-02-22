# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRococo(RPackage):
	"""Robust Rank Correlation Coefficient and Test

	Provides the robust gamma rank correlation coefficient as introduced by
	     Bodenhofer, Krone, and Klawonn (2013) <DOI:10.1016/j.ins.2012.11.026>
	     along with a permutation-based rank correlation test.
	     The rank correlation coefficient and the test are explicitly
	     designed for dealing with noisy numerical data.
	"""
	
	homepage = "http://www.bioinf.jku.at/software/rococo/"
	cran = "rococo" 

	version("1.1.7", md5="6b49bf706d17f8d2d6bfe396ee3efe68")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
