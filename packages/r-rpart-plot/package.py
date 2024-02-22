# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpartPlot(RPackage):
	"""Plot 'rpart' Models: An Enhanced Version of 'plot.rpart'.

	Plot 'rpart' models. Extends plot.rpart() and text.rpart() in the 'rpart'
	package."""

	cran = "rpart.plot"

	version("3.1.1", md5="5107258efdc312dfe709fa98babc1629")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rpart@4.1.15:", type=("build", "run"))
