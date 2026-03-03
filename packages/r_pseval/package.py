# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPseval(RPackage):
	"""Methods for Evaluating Principal Surrogates of Treatment
Response

	Contains the core methods for the evaluation of principal
    surrogates in a single clinical trial. Provides a flexible interface for
    defining models for the risk given treatment and the surrogate, the models
    for integration over the missing counterfactual surrogate responses, and the
    estimation methods. Estimated maximum likelihood and pseudo-score can be used
    for estimation, and the bootstrap for inference. A variety of post-estimation
    summary methods are provided, including print, summary, plot, and testing.
	"""
	
	cran = "pseval" 

	version("1.3.1", md5="ffc672eb4910094f59a0ace8c0c48a4c")

	depends_on("r-survival", type=("build", "run"))
