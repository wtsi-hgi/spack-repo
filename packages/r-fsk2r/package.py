# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsk2r(RPackage):
	"""An Interface Between the 'FSKX' Standard and 'R'

	Functions for importing, creating, editing and
    exporting 'FSK' files <https://foodrisklabs.bfr.bund.de/fskx-food-safety-knowledge-exchange-format/>
    using the 'R' programming environment. Furthermore, it enables users
    to run simulations contained in the 'FSK' files and visualize the results.
	"""
	
	cran = "FSK2R" 

	version("0.1.3", md5="3f73ff63e59b4e114e048b307b04f564")

	depends_on("r-xml@3.98:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.8:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-tidyr@0.7.2:", type=("build", "run"))
	depends_on("r-rlang@0.3.0.1:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-readtext@0.7.1:", type=("build", "run"))
	depends_on("r-zip@2.0.4:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-rjson@0.2.20:", type=("build", "run"))
	depends_on("r-shiny@1.3.2:", type=("build", "run"))
	depends_on("r-r-utils@2.9:", type=("build", "run"))
