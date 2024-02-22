# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoc2concrete(RPackage):
	"""Measuring Concreteness in Natural Language

	Models for detecting concreteness in natural language. This package is built in support of Yeomans (2021) <doi:10.1016/j.obhdp.2020.10.008>, which reviews linguistic models of concreteness in several domains. Here, we provide an implementation of the best-performing domain-general model (from Brysbaert et al., (2014) <doi:10.3758/s13428-013-0403-5>) as well as two pre-trained models for the feedback and plan-making domains.
	"""
	
	cran = "doc2concrete" 

	version("0.6.0", md5="a8ea6ad8e50ada3cff8af9a0a600ae02")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-english", type=("build", "run"))
	depends_on("r-textstem", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
