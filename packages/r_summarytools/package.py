# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSummarytools(RPackage):
	"""Tools to Quickly and Neatly Summarize Data

	Data frame summaries, cross-tabulations,
  weight-enabled frequency tables and common descriptive
  (univariate) statistics in concise tables available in a
  variety of formats (plain ASCII, Markdown and HTML). A good 
  point-of-entry for exploring data, both for experienced
  and new R users.
	"""
	
	homepage = "https://github.com/dcomtois/summarytools"
	cran = "summarytools" 

	version("1.0.1", md5="597574551ea4535ebec79a8a24b4f9c3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-rapportools", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
