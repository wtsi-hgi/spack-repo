# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSotkanet(RPackage):
	"""Sotkanet Open Data Access and Analysis

	Access statistical information on welfare and health in Finland 
    from the Sotkanet open data portal <https://sotkanet.fi/sotkanet/fi/index>.
	"""
	
	homepage = "https://ropengov.github.io/sotkanet/"
	cran = "sotkanet" 

	version("0.9.79", md5="855ad5411d79d969f3cbccfa7d7cfec0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
