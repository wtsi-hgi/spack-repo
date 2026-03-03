# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGptstudio(RPackage):
	"""Use Large Language Models Directly in your Development
Environment

	Large language models are readily accessible via API. This
    package lowers the barrier to use the API inside of your development
    environment.  For more on the API, see
    <https://platform.openai.com/docs/introduction>.
	"""
	
	homepage = "https://github.com/MichelNivard/gptstudio"
	cran = "gptstudio" 

	version("0.3.0", md5="395b2f5e16580e7af84b0d00c4af573c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-bslib@0.4.2:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi@0.12:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shiny-i18n", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
