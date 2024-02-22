# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParameters(RPackage):
	"""Processing of Model Parameters

	Utilities for processing the parameters of various
    statistical models. Beyond computing p values, CIs, and other indices
    for a wide variety of models (see list of supported models using the
    function 'insight::supported_models()'), this package implements
    features like bootstrapping or simulating of parameters and models,
    feature reduction (feature extraction and variable selection) as well
    as functions to describe data and variable characteristics (e.g.
    skewness, kurtosis, smoothness or distribution).
	"""
	
	homepage = "https://easystats.github.io/parameters/"
	cran = "parameters" 

	version("0.21.5", md5="b008bc6ecb1a56c6cbc9cc316e6cec75")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr@0.13.1:", type=("build", "run"))
	depends_on("r-datawizard@0.9.1:", type=("build", "run"))
	depends_on("r-insight@0.19.8:", type=("build", "run"))
