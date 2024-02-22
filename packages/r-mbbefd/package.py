# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbbefd(RPackage):
	"""Maxwell Boltzmann Bose Einstein Fermi Dirac Distribution and
Destruction Rate Modelling

	Distributions that are typically used for exposure rating in
             general insurance, in particular to price reinsurance contracts.
             The vignette shows code snippets to fit the distribution to
             empirical data. See, e.g., Bernegger (1997) <doi:10.2143/AST.27.1.563208>
             freely available on-line.
	"""
	
	homepage = "https://github.com/spedygiorgio/mbbefd"
	cran = "mbbefd" 

	version("0.8.11", md5="d46989bf4255bf6d7b56daa54374106b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fitdistrplus@1.1.4:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
