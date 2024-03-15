# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDownloadthis(RPackage):
	"""Implement Download Buttons in 'rmarkdown'

	Implement download buttons in HTML output from 'rmarkdown' without the need for 'runtime:shiny'.
	"""
	
	homepage = "https://github.com/fmmattioni/downloadthis"
	cran = "downloadthis" 

	version("0.3.3", md5="b6736975730c8c47c41a4acf6a2254f8")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
