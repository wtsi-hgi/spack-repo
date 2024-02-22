# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmcdm(RPackage):
	"""Hidden Markov Cognitive Diagnosis Models for Learning

	Fitting hidden Markov models of learning under the cognitive diagnosis framework.
  The estimation of the hidden Markov diagnostic classification model,
  the first order hidden Markov model, the reduced-reparameterized unified learning model,
  and the joint learning model for responses and response times.
	"""
	
	homepage = "https://github.com/tmsalab/hmcdm"
	cran = "hmcdm" 

	version("2.1.1", md5="f9f745bc13bd1c950bddb3887f00fd0f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bayesplot@1.9:", type=("build", "run"))
	depends_on("r-rstantools@1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
