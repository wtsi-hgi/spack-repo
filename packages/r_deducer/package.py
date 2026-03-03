# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeducer(RPackage):
	"""A Data Analysis GUI for R

	An intuitive, cross-platform graphical data analysis system. It uses menus and dialogs to guide the user efficiently through the data manipulation and analysis process, and has an excel like spreadsheet for easy data frame visualization and editing. Deducer works best when used with the Java based R GUI JGR, but the dialogs can be called from the command line. Dialogs have also been integrated into the Windows Rgui.
	"""
	
	homepage = "http://www.deducer.org/manual.html"
	cran = "Deducer" 

	version("0.7-9", md5="6ff1781914e7fdd197d8382dae134e63")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-jgr@1.7.10:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-effects", type=("build", "run"))
	depends_on("openjdk@1.4:", type=("build", "link", "run"))
