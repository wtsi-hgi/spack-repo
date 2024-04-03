# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnewsflow(RPackage):
	"""Tools for Comparing Text Messages Across Time and Media

	A collection of tools for measuring the similarity of text messages and tracing the flow of messages over
    time and across media. 
	"""
	
	cran = "RNewsflow" 

	version("1.2.8", md5="c3fbda8c6c9cf6dd0a8febf5c298273e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-igraph@1.3.4:", type=("build", "run"))
	depends_on("r-matrix@1.5:", type=("build", "run"))
	depends_on("r-stringi@1.7.8:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-wordcloud@2.6:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-quanteda@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp@1.0.9:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.2:", type=("build", "run"))
	depends_on("r-rcppprogress@0.4.2:", type=("build", "run"))
