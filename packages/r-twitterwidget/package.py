# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwitterwidget(RPackage):
	"""Render a Twitter Status in R Markdown Pages

	Include the Twitter status widgets in HTML pages created
  using R markdown. The package uses the Twitter javascript APIs to
  embed in your document Twitter cards associated to specific statuses.
  The main targets are regular HTML pages or dashboards.
	"""
	
	homepage = "https://github.com/guivo/twitterwidget"
	cran = "twitterwidget" 

	version("0.1.1", md5="b0e98f418836354590f46b51e0b7008d")

	depends_on("r-htmlwidgets", type=("build", "run"))
