# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyWorker(RPackage):
	"""Delegate Jobs for Shiny Web Applications

	It allows you to delegate heavy computation tasks
    to a separate process, such that it does not freeze your Shiny app.
	"""
	
	cran = "shiny.worker" 

	version("0.0.1", md5="a63d82911bc8876bb42e1bfc4a24d7db")

	depends_on("r-future", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
