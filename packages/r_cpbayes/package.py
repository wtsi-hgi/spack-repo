# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpbayes(RPackage):
	"""Bayesian Meta Analysis for Studying Cross-Phenotype Genetic
Associations

	A Bayesian meta-analysis method for studying cross-phenotype
    genetic associations. It uses summary-level data across multiple phenotypes to
    simultaneously measure the evidence of aggregate-level pleiotropic association
    and estimate an optimal subset of traits associated with the risk locus. CPBayes
    is based on a spike and slab prior. The methodology is available from: A Majumdar, T Haldar, S Bhattacharya, JS Witte (2018) <doi:10.1371/journal.pgen.1007139>.
	"""
	
	homepage = "https://github.com/ArunabhaCodes/CPBayes"
	cran = "CPBayes" 

	version("1.1.0", md5="2d98ee2fa29085a929b2e1341f69f129")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
