# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbres(RPackage):
	"""Exploration of Multiple Biomarker Responses using Effect Size

	Summarize multiple biomarker responses of aquatic organisms to
    contaminants using Cliff’s delta, as described in Pham & Sokolova (2023)
    <doi:10.1002/ieam.4676>.
	"""
	
	cran = "mbRes" 

	version("0.1.7", md5="7458200c09d701275b3913d54f883219")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.1:", type=("build", "run"))
	depends_on("r-cowplot@1.1.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
