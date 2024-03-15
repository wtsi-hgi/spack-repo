# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChouca(RPackage):
	"""A Stochastic Cellular Automaton Engine

	An engine for stochastic cellular automata. It provides a high-level
  interface to declare a model, which can then be simulated by various backends
  (Genin et al. (2023) <doi:10.1101/2023.11.08.566206>).
	"""
	
	homepage = "https://github.com/alexgenin/chouca"
	cran = "chouca" 

	version("0.1.99", md5="f3ca7f7cbeb583834534f8ae3cff2a0b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
