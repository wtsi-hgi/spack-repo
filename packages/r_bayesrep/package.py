# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesrep(RPackage):
	"""Bayesian Analysis of Replication Studies

	Provides tools for the analysis of replication studies using Bayes factors (Pawel and Held, 2022) <doi:10.1111/rssb.12491>.
	"""
	
	homepage = "https://github.com/SamCH93/BayesRep"
	cran = "BayesRep" 

	version("0.42.2", md5="fbd0be01897f6efe0e6714aaef340f29")

	depends_on("r-lamw", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
