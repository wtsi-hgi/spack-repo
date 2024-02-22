# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPxweb(RPackage):
	"""R Interface to PXWEB APIs

	Generic interface for the PX-Web/PC-Axis API. The
    PX-Web/PC-Axis API is used by organizations such as Statistics Sweden
    and Statistics Finland to disseminate data. The R package can interact
    with all PX-Web/PC-Axis APIs to fetch information about the data
    hierarchy, extract metadata and extract and parse statistics to R
    data.frame format. PX-Web is a solution to disseminate PC-Axis data
    files in dynamic tables on the web.  Since 2013 PX-Web contains an API
    to disseminate PC-Axis files.
	"""
	
	homepage = "https://github.com/rOpenGov/pxweb/"
	cran = "pxweb" 

	version("0.17.0", md5="e12a2de78eb600cdc7659f292d5fed71")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
