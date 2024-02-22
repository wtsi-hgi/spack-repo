# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYhatr(RPackage):
	"""R Binder for the Yhat API

	Deploy, maintain, and invoke models via the Yhat
    REST API.
	"""
	
	homepage = "https://github.com/yhat/yhatr"
	cran = "yhatr" 

	version("0.15.1", md5="eac14131adf263b52b8bc56ad1d0fe95")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
