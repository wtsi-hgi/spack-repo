# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearnr(RPackage):
	"""Interactive Tutorials for R

	Create interactive tutorials using R Markdown. Use a
    combination of narrative, figures, videos, exercises, and quizzes to
    create self-paced tutorials for learning about R and R packages.
	"""
	
	homepage = "https://rstudio.github.io/learnr/"
	cran = "learnr" 

	version("0.11.5", md5="b0965e4b63241e85a8dd5f0a9d6074ba")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ellipsis@0.2.0.1:", type=("build", "run"))
	depends_on("r-evaluate", type=("build", "run"))
	depends_on("r-htmltools@0.3.5:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr@1.31:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-markdown@1.3:", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-renv@0.8:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown@1.12:", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
