# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebanalytics(RPackage):
	"""Web Server Log Analysis

	Provides Apache and IIS log analytics for transaction performance, client populations and workload definitions.
	"""
	
	homepage = "https://github.com/gregfrog/WebAnalytics"
	cran = "WebAnalytics" 

	version("0.9.12", md5="af93afbc55dff56b2cad8471affa2e7f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-xtable@1.8.4:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-brew@1.0.6:", type=("build", "run"))
	depends_on("r-fs@1.5.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-digest@0.6.29:", type=("build", "run"))
	depends_on("r-tinytex@0.37:", type=("build", "run"))
	depends_on("r-uaparserjs@0.3.5:", type=("build", "run"))
