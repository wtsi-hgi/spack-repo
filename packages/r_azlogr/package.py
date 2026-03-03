# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzlogr(RPackage):
	"""Logging in 'R' and Post to 'Azure Log Analytics' Workspace

	It extends the functionality of 'logger' package. Additional
    logging metadata can be configured to be collected. Logging messages are
    displayed on console and optionally they are sent to 'Azure Log Analytics'
    workspace in real-time.
	"""
	
	homepage = "https://atalv.github.io/azlogr/"
	cran = "azlogr" 

	version("0.0.6", md5="d1ccd3201b044cfd88dc8d072dac7cef")
	version("0.0.5", md5="ac37e5c0bc60dc4bf8059442ef94f50c")

	depends_on("r-catools", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-logger@0.2:", type=("build", "run"))
