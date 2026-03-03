# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpoxy(RPackage):
	"""String Interpolation for Documents, Reports and Apps

	Extra strength 'glue' for data-driven templates. String
    interpolation for 'Shiny' apps or 'R Markdown' and 'knitr'-powered
    'Quarto' documents, built on the 'glue' and 'whisker' packages.
	"""
	
	homepage = "https://pkg.garrickadenbuie.com/epoxy/"
	cran = "epoxy" 

	version("1.0.0", md5="2f0f8a6877c72c7b1b9118a8abe4b238")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-and", type=("build", "run"))
	depends_on("r-glue@1.5:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr@1.37:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
