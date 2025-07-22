# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTkwidgets(RPackage):
	"""R based tk widgets

	Widgets to provide user interfaces. tcltk should have been installed for the widgets to run.
	"""
	
	bioc = "tkWidgets" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tkWidgets_1.80.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tkWidgets/tkWidgets_1.80.0.tar.gz"]

	version("1.80.0", sha256="3267fca54e0f0e1232365e8bf71b104e7febfc5cb47d5be8304da857a9cb4885")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-widgettools@1.1.7:", type=("build", "run"))
	depends_on("r-dyndoc@1.3:", type=("build", "run"))
