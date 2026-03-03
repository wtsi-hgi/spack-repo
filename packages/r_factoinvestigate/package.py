# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactoinvestigate(RPackage):
	"""Automatic Description of Factorial Analysis

	Brings a set of tools to help and automatically realise the description of principal component analyses (from 'FactoMineR' functions). Detection of existing outliers, identification of the informative components, graphical views and dimensions description are performed threw dedicated functions. The Investigate() function performs all these functions in one, and returns the result as a report document (Word, PDF or HTML).
	"""
	
	homepage = "http://factominer.free.fr/reporting/"
	cran = "FactoInvestigate" 

	version("1.9", md5="5fd403a3d6366f745c1394500409363a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
