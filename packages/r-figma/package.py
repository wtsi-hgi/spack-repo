# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFigma(RPackage):
	"""Web Client/Wrapper to the 'Figma API'

	An easy-to-use web client/wrapper for the 'Figma API' <https://www.figma.com/developers/api>. 
  It allows you to bring all data from a 'Figma' file to your 'R' session. This includes the data of all objects
  that you have drawn in this file, and their respective canvas/page metadata.
	"""
	
	homepage = "https://github.com/pedropark99/figma"
	cran = "figma" 

	version("0.2.0", md5="69e1ebec985ec11bc47f5fe598d9ee77")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble@3.0.5:", type=("build", "run"))
