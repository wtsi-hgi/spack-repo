# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgdraw(RPackage):
	"""Generate Random Samples from the Polya-Gamma Distribution

	Generates random samples from the Polya-Gamma distribution using an implementation of the algorithm described in J. Windle's PhD thesis (2013) <https://repositories.lib.utexas.edu/bitstream/handle/2152/21842/WINDLE-DISSERTATION-2013.pdf>. The underlying implementation is in C.
	"""
	
	cran = "pgdraw" 

	version("1.1", md5="1e36c651849bf3ff87d8446bebfbe1b3")

	depends_on("r-rcpp", type=("build", "run"))
