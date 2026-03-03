# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvylme(RPackage):
	"""Linear Mixed Models for Complex Survey Data

	Linear mixed models for complex survey data, by pairwise composite likelihood, as described in Lumley & Huang (2023) <arXiv:2311.13048>. Supports nested and crossed random effects, and correlated random effects as in genetic models.  Allows for multistage sampling and for other designs where pairwise sampling probabilities are specified or can be calculated. 
	"""
	
	cran = "svylme" 

	version("1.5-1", md5="e88968110d90345d414e8f9c3fec0b29")

	depends_on("r-survey", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
