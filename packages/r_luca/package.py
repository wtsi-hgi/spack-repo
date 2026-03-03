# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLuca(RPackage):
	"""Likelihood Inference from Case-Control Data under Covariate
Assumptions

	Likelihood inference under covariate assumptions (LUCA) in case-control studies of a rare disease assuming independence or simple dependence of genetic and
        non-genetic covariates.
	"""
	
	homepage = "https://sfustatgen.github.io/research/luca.html"
	cran = "luca" 

	version("1.0-6", md5="65572ef4ddc64fd4e94bb273288cf005")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-genetics", type=("build", "run"))
