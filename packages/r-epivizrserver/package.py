# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpivizrserver(RPackage):
	"""WebSocket server infrastructure for epivizr apps and packages

	This package provides objects to manage WebSocket connections to epiviz apps. Other epivizr package use this infrastructure.
	"""
	
	homepage = "https://epiviz.github.io"
	bioc = "epivizrServer" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/epivizrServer_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/epivizrServer/epivizrServer_1.30.0.tar.gz"]

	version("1.30.0", md5="4bc67106aa169616232174c422fb6e2b")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-httpuv@1.3:", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-mime@0.2:", type=("build", "run"))
