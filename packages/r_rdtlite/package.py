# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdtlite(RPackage):
	"""Provenance Collector

	Defines functions that can be used to collect provenance as
  an 'R' script executes or during a console session. The output is a text 
  file in 'PROV-JSON' format.
	"""
	
	homepage = "https://github.com/End-to-end-provenance/rdtLite"
	cran = "rdtLite" 

	version("1.4", md5="7f1229f80b8c93159edb337d758c9909")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-provviz@1.0.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
