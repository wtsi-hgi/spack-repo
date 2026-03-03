# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBender(RPackage):
	"""Bender Client

	R client for Bender Hyperparameters optimizer : <https://bender.dreem.com>
    The R client allows you to communicate with the Bender API and therefore submit some new trials within your R script itself.
	"""
	
	cran = "bender" 

	version("0.1.1", md5="5774f0052c60f250310eb61a491c7dff")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
