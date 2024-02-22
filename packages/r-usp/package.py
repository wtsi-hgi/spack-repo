# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsp(RPackage):
	"""U-Statistic Permutation Tests of Independence for all Data Types

	Implements various independence tests for discrete, continuous, and infinite-dimensional data. The tests are based on a U-statistic permutation test, the USP of Berrett, Kontoyiannis and Samworth (2020) <arXiv:2001.05513>, and shown to be minimax rate optimal in a wide range of settings. As the permutation principle is used, all tests have exact, non-asymptotic Type I error control at the nominal level.
	"""
	
	cran = "USP" 

	version("0.1.2", md5="9795fbc43e604fb8b40c319f588e28e4")

	depends_on("r-rdpack", type=("build", "run"))
