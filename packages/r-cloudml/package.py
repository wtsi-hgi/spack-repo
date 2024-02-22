# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCloudml(RPackage):
	"""Interface to the Google Cloud Machine Learning Platform

	Interface to the Google Cloud Machine Learning Platform
  <https://cloud.google.com/ml-engine>, which provides cloud tools for training machine
  learning models.
	"""
	
	cran = "cloudml" 

	version("0.6.1", md5="d09f5a0f192f7b9d04c809cc871e6d08")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-tfruns@1.3:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-packrat", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("python@2.7:", type=("build", "link", "run"))
