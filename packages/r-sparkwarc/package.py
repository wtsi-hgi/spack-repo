# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparkwarc(RPackage):
	"""Load WARC Files into Apache Spark

	Load WARC (Web ARChive) files into Apache Spark using 'sparklyr'. This
    allows to read files from the Common Crawl project <http://commoncrawl.org/>.
	"""
	
	cran = "sparkwarc" 

	version("0.1.6", md5="5cd68a1d2722dc4d2081d12f5ef46772")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-sparklyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
