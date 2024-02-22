# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromote(RPackage):
	"""Headless Chrome Web Browser Interface

	An implementation of the 'Chrome DevTools Protocol', for
    controlling a headless Chrome web browser.
	"""
	
	homepage = "https://rstudio.github.io/chromote/"
	cran = "chromote" 

	version("0.2.0", md5="98aac34a13ae6dd8f5187d25cb7a1149")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-later@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-promises@1.1.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-websocket@1.2:", type=("build", "run"))
