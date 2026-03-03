# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLilrhino(RPackage):
	"""For Implementation of Feed Reduction, Learning Examples, NLP and
Code Management

	This is for code management functions, NLP tools, a Monty Hall simulator, and for implementing my own variable reduction technique called Feed Reduction. The Feed Reduction technique is not yet published, but is merely a tool for implementing a series of binary neural networks meant for reducing data into N dimensions, where N is the number of possible values of the response variable.
	"""
	
	cran = "LilRhino" 

	version("1.2.2", md5="f4ab56c3931d633e81edc24de5e8e41c")

	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
