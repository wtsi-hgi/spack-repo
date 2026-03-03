# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnrichwith(RPackage):
	"""Methods to Enrich R Objects with Extra Components

	Provides the "enrich" method to enrich list-like R objects with new, relevant components. The current version has methods for enriching objects of class 'family', 'link-glm', 'lm', 'glm' and 'betareg'. The resulting objects preserve their class, so all methods associated with them still apply. The package also provides the 'enriched_glm' function that has the same interface as 'glm' but results in objects of class 'enriched_glm'. In addition to the usual components in a `glm` object, 'enriched_glm' objects carry an object-specific simulate method and functions to compute the scores, the observed and expected information matrix, the first-order bias, as well as model densities, probabilities, and quantiles at arbitrary parameter values. The package can also be used to produce customizable source code templates for the structured implementation of methods to compute new components and enrich arbitrary objects.
	"""
	
	homepage = "https://github.com/ikosmidis/enrichwith"
	cran = "enrichwith" 

	version("0.3.1", md5="df897db7893d5919f4dde4ca82256410")

	depends_on("r@3:", type=("build", "run"))
