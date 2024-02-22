# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPromote(RPackage):
	"""Client for the 'Alteryx Promote' API

	Deploy, maintain, and invoke predictive models using the 'Alteryx
    Promote' REST API.  'Alteryx Promote' is available at the URL:
    <https://www.alteryx.com/products/alteryx-promote>.
	"""
	
	homepage = "https://github.com/alteryx/promote-r-client"
	cran = "promote" 

	version("1.1.1", md5="5f12f0fa4a06849d2dec140524e3adb7")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
