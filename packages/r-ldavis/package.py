# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdavis(RPackage):
	"""Interactive Visualization of Topic Models

	Tools to create an interactive web-based visualization of a
    topic model that has been fit to a corpus of text data using
    Latent Dirichlet Allocation (LDA). Given the estimated parameters of
    the topic model, it computes various summary statistics as input to
    an interactive visualization built with D3.js that is accessed via
    a browser. The goal is to help users interpret the topics in their
    LDA topic model.
	"""
	
	homepage = "https://github.com/cpsievert/LDAvis"
	cran = "LDAvis" 

	version("0.3.2", md5="d2fbbd6e29f04ca641e13b8a11525573")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
