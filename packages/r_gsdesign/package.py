# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsdesign(RPackage):
	"""Group Sequential Design

	Derives group sequential clinical trial designs and describes
    their properties. Particular focus on time-to-event, binary, and
    continuous outcomes. Largely based on methods described in
    Jennison, Christopher and Turnbull, Bruce W., 2000,
    "Group Sequential Methods with Applications to Clinical Trials"
    ISBN: 0-8493-0316-8.
	"""
	
	homepage = "https://keaven.github.io/gsDesign/"
	cran = "gsDesign" 

	version("3.6.1", md5="37cb49fb654ddaf866b563368a3fb1b1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r2rtf", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
