# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdatuning(RPackage):
	"""Tuning of the Latent Dirichlet Allocation Models Parameters

	For this first version only metrics to estimate the best fitting
    number of topics are implemented.
	"""
	
	homepage = "https://github.com/nikita-moor/ldatuning"
	cran = "ldatuning" 

	version("1.0.2", md5="980c35fcf07e6d5df68843a3bcfbd468")

	depends_on("r-topicmodels", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
