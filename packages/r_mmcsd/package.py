# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmcsd(RPackage):
	"""Modeling Complex Longitudinal Data in a Quick and Easy Way

	Matching longitudinal methodology models with complex sampling design. It fits fixed
    and random effects models and covariance structured models so far. It also
    provides tools to perform statistical tests considering these specifications as described in : Pacheco, P. H. (2021). "Modeling complex longitudinal data in R: development of a statistical package." <https://repositorio.ufjf.br/jspui/bitstream/ufjf/13437/1/pedrohenriquedemesquitapacheco.pdf>.
	"""
	
	cran = "Mmcsd" 

	version("1.0.0", md5="92f61882b0cf595a37f7a7b76262e145")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
