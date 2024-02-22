# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVitae(RPackage):
	"""Curriculum Vitae for R Markdown

	Provides templates and functions to simplify the production and maintenance of curriculum vitae.
	"""
	
	homepage = "https://pkg.mitchelloharawild.com/vitae/"
	cran = "vitae" 

	version("0.5.4", md5="f2e12e6fb809851d7081e41840324997")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rmarkdown@2.2:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs@0.3.3:", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("pandoc@2.7:", type=("build", "link", "run"))
