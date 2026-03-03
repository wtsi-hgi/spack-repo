# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWbsd(RPackage):
	"""Wild Bootstrap Size Diagnostics

	Implements the diagnostic "theta" developed in Poetscher and Preinerstorfer (2020) "How Reliable are Bootstrap-based Heteroskedasticity Robust Tests?" <arXiv:2005.04089>. This diagnostic can be used to detect and weed out bootstrap-based procedures that provably have size equal to one for a given testing problem. The implementation covers a large variety of bootstrap-based procedures, cf. the above mentioned article for details. A function for computing bootstrap p-values is provided.
	"""
	
	cran = "wbsd" 

	version("1.0.0", md5="44fdd30600546fd1b7dd8042adbf672b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
