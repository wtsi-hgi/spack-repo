# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQmethod(RPackage):
	"""Analysis of Subjective Perspectives Using Q Methodology

	Analysis of Q methodology, used to identify distinct perspectives existing within a group.
  This methodology is used across social, health and environmental sciences to understand diversity of attitudes, discourses, or decision-making styles (for more information, see <https://qmethod.org/>).
  A single function runs the full analysis. Each step can be run separately using the corresponding functions: for automatic flagging of Q-sorts (manual flagging is optional), for statement scores, for distinguishing and consensus statements, and for general characteristics of the factors.
  The package allows to choose either principal components or centroid factor extraction, manual or automatic flagging, a number of mathematical methods for rotation (or none), and a number of correlation coefficients for the initial correlation matrix, among many other options.
  Additional functions are available to import and export data (from raw *.CSV, 'HTMLQ' and 'FlashQ' *.CSV, 'PQMethod' *.DAT and 'easy-htmlq' *.JSON files), to print and plot, to import raw data from individual *.CSV files, and to make printable cards.
  The package also offers functions to print Q cards and to generate Q distributions for study administration.
  See further details in the package documentation, and in the web pages below, which include a cookbook, guidelines for more advanced analysis (how to perform manual flagging or change the sign of factors), data management, and a graphical user interface (GUI) for online and offline use.
	"""
	
	homepage = "https://github.com/aiorazabala/qmethod"
	cran = "qmethod" 

	version("1.8.4", md5="cfaa888ea5d9062b1dff257e1655e962")

	depends_on("r-psych", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
