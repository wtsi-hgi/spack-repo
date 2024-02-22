# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBandit(RPackage):
	"""Functions for Simple a/B Split Test and Multi-Armed Bandit
Analysis

	A set of functions for doing analysis of A/B split test data and web metrics in general.
	"""
	
	cran = "bandit" 

	version("0.5.1", md5="b1b280ca677ffe9a301ec08e11eb70a8")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-gam@1.9:", type=("build", "run"))
