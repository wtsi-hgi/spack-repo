# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLvplot(RPackage):
	"""Letter Value 'Boxplots'

	Implements the letter value 'boxplot' which extends the
    standard 'boxplot' to deal with both larger and smaller number of data
    points by dynamically selecting the appropriate number of letter
    values to display.
	"""
	
	cran = "lvplot" 

	version("0.2.1", md5="ef7a73312a71ba035f8f5388f12d9f79")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
