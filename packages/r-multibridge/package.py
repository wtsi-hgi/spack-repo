# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultibridge(RPackage):
	"""Evaluating Multinomial Order Restrictions with Bridge Sampling

	Evaluate hypotheses concerning the distribution of multinomial
  proportions using bridge sampling. The bridge sampling routine is able to
  compute Bayes factors for hypotheses that entail inequality constraints,
  equality constraints, free parameters, and mixtures of all three. These
  hypotheses are tested against the encompassing hypothesis, that all parameters
  vary freely or against the null hypothesis that all category proportions are equal.
  For more information see Sarafoglou et al. (2020) <doi:10.31234/osf.io/bux7p>.
	"""
	
	homepage = "https://github.com/asarafoglou/multibridge/"
	cran = "multibridge" 

	version("1.2.0", md5="e4475897fc213509b7cacaf1c97e68a9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-brobdingnag", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("mpfr", type=("build", "link", "run"))
	depends_on("gmp", type=("build", "link", "run"))
