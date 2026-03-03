# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyquiz(RPackage):
	"""Create Interactive Quizzes in 'shiny'

	Simple and flexible quizzes in 'shiny'. Easily create quizzes from various pre-built question and choice types or create your own using 'htmltools' and 'shiny' packages as building blocks. Integrates with larger 'shiny' applications. Ideal for non-web-developers such as educators, data scientists, and anyone who wants to assess responses interactively in a small form factor.
	"""
	
	homepage = "https://priism-center.github.io/shinyquiz/"
	cran = "shinyquiz" 

	version("0.0.1", md5="9803543e48f54f22def2ecd30ce079b8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-fontawesome@0.5:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-htmltools@0.5.5:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-reactable@0.4.4:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-stringi@1.7.12:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
