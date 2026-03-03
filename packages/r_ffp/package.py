# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfp(RPackage):
	"""Fully Flexible Probabilities for Stress Testing and Portfolio
Construction

	Implements numerical entropy-pooling for portfolio construction and 
    scenario analysis as described in Meucci, Attilio (2008) and Meucci, Attilio (2010) 
    <doi:10.2139/ssrn.1696802>.
	"""
	
	homepage = "https://github.com/Reckziegel/FFP"
	cran = "ffp" 

	version("0.2.2", md5="46201bfdea745944c2b8db4b29d919cc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-forcats@0.5.2:", type=("build", "run"))
	depends_on("r-ggdist@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-lubridate@1.8:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
	depends_on("r-tidyr@1.2.1:", type=("build", "run"))
	depends_on("r-vctrs@0.4.1:", type=("build", "run"))
	depends_on("r-nloptr@2.0.3:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-nlcoptim@0.6:", type=("build", "run"))
