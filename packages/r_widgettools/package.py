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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/widgetTools_1.80.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/widgetTools/widgetTools_1.80.0.tar.gz"]

	version("1.80.0", md5="bb5358a7e064436aa744ffb098a9c0ec")

	depends_on("r@2.4:", type=("build", "run"))
