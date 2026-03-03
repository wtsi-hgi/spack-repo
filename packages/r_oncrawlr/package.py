# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncrawlr(RPackage):
	"""Machine Learning for S.E.O

	Measures different aspects of page content, structure and performance for SEO (Search Engine Optimization).
    Aspects covered include HTML tags used in SEO, duplicate and near-duplicate content, structured data, on-site linking structure and popularity transfer, and many other amazing things. 
    This package can be used to generate a real, full SEO audit report, which serves to detect errors or inefficiencies on a page that can be corrected in order to optimise its performance on search engines.
	"""
	
	cran = "oncrawlR" 

	version("0.2.0", md5="6af1b86e706cb670ecd8171d5a99089a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcurl@1.8:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-xgboost@0.8:", type=("build", "run"))
	depends_on("r-proc@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-caret@6:", type=("build", "run"))
	depends_on("r-dalex@0.3:", type=("build", "run"))
	depends_on("r-rlist@0.4.6:", type=("build", "run"))
	depends_on("r-readr@1.3:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-formattable@0.2:", type=("build", "run"))
	depends_on("r-sparkline@0.2:", type=("build", "run"))
	depends_on("r-webshot@0.5:", type=("build", "run"))
	depends_on("r-e1071@1.7:", type=("build", "run"))
	depends_on("r-pdp@0.7:", type=("build", "run"))
	depends_on("r-fs@1.3:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.2:", type=("build", "run"))
	depends_on("r-htmltools@0.3.5:", type=("build", "run"))
	depends_on("r-rjson@0.2.20:", type=("build", "run"))
