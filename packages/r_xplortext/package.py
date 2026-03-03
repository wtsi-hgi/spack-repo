# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXplortext(RPackage):
	"""Statistical Analysis of Textual Data

	Provides a set of functions devoted to multivariate exploratory statistics on textual data. Classical methods such as correspondence analysis and agglomerative hierarchical clustering are available. Chronologically constrained agglomerative hierarchical clustering enriched with labelled-by-words trees is offered. Given a division of the corpus into parts, their characteristic words and documents are identified. Further, accessing to 'FactoMineR' functions is very easy. Two of them are relevant in textual domain. MFA() addresses multiple lexical table allowing applications such as dealing with multilingual corpora as well as simultaneously analyzing both open-ended and closed questions in surveys. See <http://xplortext.unileon.es> for examples.
	"""
	
	homepage = "https://xplortext.unileon.es"
	cran = "Xplortext" 

	version("1.5.3", md5="a86bc0f69988cef73c3362df1b8a7362")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-factominer@2.8:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-tm@0.7.11:", type=("build", "run"))
	depends_on("r-flexclust@1.4.1:", type=("build", "run"))
	depends_on("r-flashclust@1.1.2:", type=("build", "run"))
	depends_on("r-ggdendro@0.1.23:", type=("build", "run"))
	depends_on("r-ggforce@0.4.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.9.3:", type=("build", "run"))
	depends_on("r-plotly@4.10.1:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-mass@7.3.58.4:", type=("build", "run"))
	depends_on("r-stringi@1.7.12:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-slam@0.1.50:", type=("build", "run"))
	depends_on("r-vegan@2.6.4:", type=("build", "run"))
