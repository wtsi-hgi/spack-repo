# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWidgettools(RPackage):
	"""Creates an interactive tcltk widget

	This packages contains tools to support the construction of tcltk widgets
	"""
	
	bioc = "widgetTools"

	version("1.86.0", commit="f7c0a637a52dd1b47aae4336bef95d40ccc88bfc")
	version("1.80.0", commit="ddf3bb3e6f2f5e622ec8a90d17173605a5c7311c")

	depends_on("r@2.4:", type=("build", "run"))
