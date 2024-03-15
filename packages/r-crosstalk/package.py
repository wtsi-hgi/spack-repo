# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrosstalk(RPackage):
	"""Inter-Widget Interactivity for HTML Widgets.

	Provides building blocks for allowing HTML widgets to communicate with each
	other, with Shiny or without (i.e. static .html files). Currently supports
	linked brushing and filtering."""

	cran = "crosstalk"

	license("MIT")

	version("1.2.1", md5="f9e4a6f7e1cb679a69a8c10059bd0ecf")

	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
