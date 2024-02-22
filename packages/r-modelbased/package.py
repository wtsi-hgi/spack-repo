# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelbased(RPackage):
	"""Estimation of Model-Based Predictions, Contrasts and Means

	Implements a general interface for model-based estimations
    for a wide variety of models (see list of supported models using the
    function 'insight::supported_models()'), used in the computation of
    marginal means, contrast analysis and predictions.
	"""
	
	homepage = "https://easystats.github.io/modelbased/"
	cran = "modelbased" 

	version("0.8.7", md5="2cf06df7469c4cb8c910533f3aca2329")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr@0.13.1:", type=("build", "run"))
	depends_on("r-datawizard@0.9.1:", type=("build", "run"))
	depends_on("r-effectsize@0.8.6:", type=("build", "run"))
	depends_on("r-insight@0.19.8:", type=("build", "run"))
	depends_on("r-parameters@0.21.3:", type=("build", "run"))
	depends_on("r-performance@0.10.8:", type=("build", "run"))
