# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbcData(RPackage):
	"""Data Only: Tools for Approximate Bayesian Computation (ABC)

	Contains data which are used by functions of the 'abc' package.
	"""
	
	cran = "abc.data" 

	version("1.1", md5="1693d5a243a991f8cf290471972a54f8")

	depends_on("r@2.10:", type=("build", "run"))
