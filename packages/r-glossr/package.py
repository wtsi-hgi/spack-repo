# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlossr(RPackage):
	"""Use Interlinear Glosses in R Markdown

	Read examples with interlinear glosses from files
    or from text and print them in a way compatible with both
    Latex and HTML outputs.
	"""
	
	homepage = "https://montesmariana.github.io/glossr/"
	cran = "glossr" 

	version("0.7.0", md5="1a80317209c6f9b50fde57948a6056b6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
