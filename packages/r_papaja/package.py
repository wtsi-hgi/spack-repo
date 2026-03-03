# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPapaja(RPackage):
	"""Prepare American Psychological Association Journal Articles with
R Markdown

	Tools to create dynamic, submission-ready manuscripts, which
  conform to American Psychological Association manuscript guidelines. We
  provide R Markdown document formats for manuscripts (PDF and Word) and
  revision letters (PDF). Helper functions facilitate reporting statistical
  analyses or create publication-ready tables and plots.
	"""
	
	homepage = "https://github.com/crsh/papaja"
	cran = "papaja" 

	version("0.1.2", md5="40aecd4c9c1ec8cdd79d8598a1ea3bbd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tinylabels@0.1:", type=("build", "run"))
	depends_on("r-bookdown@0.9.1:", type=("build", "run"))
	depends_on("r-broom@0.7:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-knitr@1.26:", type=("build", "run"))
	depends_on("r-rmarkdown@2.4:", type=("build", "run"))
	depends_on("r-rmdfiltr@0.1.3:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
