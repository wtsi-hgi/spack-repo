# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppjagger(RPackage):
	"""An R Wrapper for Jagger

	A wrapper for Jagger, a morphological analyzer proposed in Yoshinaga (2023) <arXiv:2305.19045>. Jagger uses patterns derived from morphological dictionaries and training data sets and applies them from the beginning of the input. This simultaneous and deterministic process enables it to effectively perform tokenization, POS tagging, and lemmatization.
	"""
	
	homepage = "https://shusei-e.github.io/RcppJagger/"
	cran = "RcppJagger" 

	version("0.0.2", md5="dd0b8eba4738bcfcd7e11eae506385fc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
