# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaehbUnit(RPackage):
	"""Basic Unit Level Model using Hierarchical Bayesian Approach

	Small area estimation unit level models (Battese-Harter-Fuller model) with a Bayesian Hierarchical approach. See also Rao & Molina (2015, ISBN:978-1-118-73578-7) and Battese et al. (1988) <doi:10.1080/01621459.1988.10478561>.
	"""
	
	homepage = "https://github.com/Alfrzlp/saeHB.unit"
	cran = "saeHB.unit" 

	version("0.1.0", md5="39c7385b388cc9787796d58432b03cf9")

	depends_on("r@3.60:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
