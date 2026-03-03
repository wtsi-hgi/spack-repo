# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTigrebrowserwriter(RPackage):
	"""'tigreBrowser' Database Writer

	Write modelling results into a database for
    'tigreBrowser', a web-based tool for browsing figures and summary
    data of independent model fits, such as Gaussian process models
    fitted for each gene or other genomic element. The browser is
    available at <https://github.com/PROBIC/tigreBrowser>.
	"""
	
	homepage = "https://github.com/PROBIC/tigreBrowserWriter"
	cran = "tigreBrowserWriter" 

	version("0.1.5", md5="75fd1b7af5cc28b8fa5a9927b72da369")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
