# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReceptiviti(RPackage):
	"""Text Analysis Through the 'Receptiviti' API

	Send text to the <https://www.receptiviti.com> API to be scored
    by all available frameworks.
	"""
	
	homepage = "https://receptiviti.github.io/receptiviti-r/"
	cran = "receptiviti" 

	version("0.1.6", md5="7dce4c8275a4ad285eb0a78f82187465")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-arrow@9:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
