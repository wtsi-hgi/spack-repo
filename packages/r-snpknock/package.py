# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnpknock(RPackage):
	"""Knockoffs for Hidden Markov Models and Genetic Data

	Generate knockoffs for genetic data and hidden Markov models.
  For more information, see the website below and the accompanying papers: 
  "Gene hunting with hidden Markov model knockoffs", Sesia et al., Biometrika, 2019, (<doi:10.1093/biomet/asy033>).
  "Multi-resolution localization of causal variants across the genome", Sesia et al., bioRxiv, 2019, (<doi:10.1101/631390>).
	"""
	
	homepage = "https://msesia.github.io/snpknock"
	cran = "SNPknock" 

	version("0.8.2", md5="015d88a39eb60a71bc47cd2e265a7b94")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
