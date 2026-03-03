# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIxplorer(RPackage):
	"""Easy DataOps for R Users

	Create and view tickets in 'gitea', a self-hosted git service <https://gitea.io>, using an 'RStudio' addin, and use helper functions to publish documentation and use git.
	"""
	
	homepage = "https://github.com/ixpantia/ixplorer"
	cran = "ixplorer" 

	version("0.2.2", md5="8172b95cc531a562a5cbc54696f5c58c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.1:", type=("build", "run"))
	depends_on("r-gitear@0.0.2:", type=("build", "run"))
	depends_on("r-kableextra@1.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-miniui@0.1.1.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-shiny-i18n@0.2:", type=("build", "run"))
	depends_on("r-shiny@1.3.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-shinywidgets@0.2.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-gert@1.5:", type=("build", "run"))
	depends_on("r-keyring@1.3:", type=("build", "run"))
