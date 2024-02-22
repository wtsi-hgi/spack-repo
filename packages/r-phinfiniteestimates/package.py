# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhinfiniteestimates(RPackage):
	"""Tools for Inference in the Presence of a Monotone Likelihood

	Proportional hazards estimation in the presence of a partially monotone likelihood has difficulties, in that finite estimators do not exist.  These difficulties are related to those arising from logistic and multinomial regression.  References for methods are given in the separate function documents.  Supported by grant NSF DMS 1712839.
	"""
	
	cran = "PHInfiniteEstimates" 

	version("2.9.5", md5="8c72c1d3ee5838fae4c7b98bf7f35384")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-coxphf", type=("build", "run"))
	depends_on("r-nph", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
