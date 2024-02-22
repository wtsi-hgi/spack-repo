# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMantaid(RPackage):
	"""A Machine-Learning Based Tool to Automate the Identification of
Biological Database IDs

	The number of biological databases is growing rapidly, but different databases use different IDs to refer to the same biological entity. The inconsistency in IDs impedes the integration of various types of biological data. To resolve the problem, we developed 'MantaID', a data-driven, machine-learning based approach that automates identifying IDs on a large scale. The 'MantaID' model's prediction accuracy was proven to be 99%, and it correctly and effectively predicted 100,000 ID entries within two minutes. 'MantaID' supports the discovery and exploitation of ID patterns from large quantities of databases. (e.g., up to 542 biological databases). An easy-to-use freely available open-source software R package, a user-friendly web application, and APIs were also developed for 'MantaID' to improve applicability. To our knowledge, 'MantaID' is the first tool that enables an automatic, quick, accurate, and comprehensive identification of large quantities of IDs, and can therefore be used as a starting point to facilitate the complex assimilation and aggregation of biological data across diverse databases.
	"""
	
	cran = "MantaID" 

	version("1.0.2", md5="3d052cba4f580e6c90c141ea7f649a0d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mlr3", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scutr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-mlr3tuning", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
