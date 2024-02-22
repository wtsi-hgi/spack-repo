# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCforward(RPackage):
	"""Forward Selection using Concordance/C-Index

	Performs forward model selection, using the C-index/concordance
  in survival analysis models. 
	"""
	
	homepage = "https://github.com/muschellij2/cforward"
	cran = "cforward" 

	version("0.1.0", md5="afcab3ce9cedacd02f4df7f701ab303c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
