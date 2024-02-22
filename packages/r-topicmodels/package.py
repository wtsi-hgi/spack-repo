# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopicmodels(RPackage):
	"""Topic Models

	Provides an interface to the C code for Latent Dirichlet
	     Allocation (LDA) models and Correlated Topics Models
	     (CTM) by David M. Blei and co-authors and the C++ code
	     for fitting LDA models using Gibbs sampling by Xuan-Hieu
	     Phan and co-authors.
	"""
	
	cran = "topicmodels" 

	version("0.2-16", md5="0f35a89632a26caad7d019f515116c21")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-tm@0.6:", type=("build", "run"))
	depends_on("gsl@1.8:", type=("build", "link", "run"))
