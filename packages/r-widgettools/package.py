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

	version("1.80.0", sha256="819b299090c78642369dadc1779be4e7cd3e76fc183e7dac5a0b87a5cb116cfe")

	depends_on("r@2.4:", type=("build", "run"))
