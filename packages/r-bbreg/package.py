# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbreg(RPackage):
	"""Bessel and Beta Regressions via Expectation-Maximization
Algorithm for Continuous Bounded Data

	Functions to fit, via Expectation-Maximization (EM) algorithm, the Bessel and Beta regressions to a data set with a bounded continuous response variable. The Bessel regression is a new and robust approach proposed in the literature. The EM version for the well known Beta regression is another major contribution of this package. See details in the references Barreto-Souza, Mayrink and Simas (2022) <doi:10.1111/anzs.12354> and Barreto-Souza, Mayrink and Simas (2020) <arXiv:2003.05157>.  
	"""
	
	cran = "bbreg" 

	version("2.0.2", md5="1b3ca45e02d7b156cfd4ba7b35e51174")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
