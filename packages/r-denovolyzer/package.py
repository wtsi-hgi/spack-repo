# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDenovolyzer(RPackage):
	"""Statistical Analyses of De Novo Genetic Variants

	An integrated toolset for the analysis of de novo (sporadic)
    genetic sequence variants. denovolyzeR implements a mutational model that
    estimates the probability of a de novo genetic variant arising in each human
    gene, from which one can infer the expected number of de novo variants in a
    given population size. Observed variant frequencies can then be compared against
    expectation in a Poisson framework. denovolyzeR provides a suite of functions
    to implement these analyses for the interpretation of de novo variation in human
    disease.
	"""
	
	homepage = "http://denovolyzeR.org"
	cran = "denovolyzeR" 

	version("0.2.0", md5="f5b28c233d6271733b74c9d0cf65e8ef")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.3:", type=("build", "run"))
	depends_on("r-reshape2@1.4:", type=("build", "run"))
