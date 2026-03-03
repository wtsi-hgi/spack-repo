# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcmbasecpp(RPackage):
	"""Fast Likelihood Calculation for Phylogenetic Comparative Models

	Provides a C++ backend for multivariate phylogenetic comparative
  models implemented in the R-package 'PCMBase'. Can be used in combination
  with 'PCMBase' to enable fast and parallel likelihood calculation. Implements
  the pruning likelihood calculation algorithm described in Mitov et al. (2018) 
  <arXiv:1809.09014>. Uses the 'SPLITT' C++ library for parallel tree traversal 
  described in Mitov and Stadler (2018) <doi:10.1111/2041-210X.13136>.
	"""
	
	homepage = "https://github.com/venelin/PCMBaseCpp"
	cran = "PCMBaseCpp" 

	version("0.1.9", md5="b8a1a0c7cc8988464dab9f0004a5ed35")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pcmbase", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
