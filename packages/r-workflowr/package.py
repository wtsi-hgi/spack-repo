# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorkflowr(RPackage):
	"""A Framework for Reproducible and Collaborative Data Science

	Provides a workflow for your analysis projects by combining
  literate programming ('knitr' and 'rmarkdown') and version control
  ('Git', via 'git2r') to generate a website containing time-stamped,
  versioned, and documented results.
	"""
	
	homepage = "https://github.com/workflowr/workflowr"
	cran = "workflowr" 

	version("1.7.1", md5="13446e8ea9a9e798ab2d0d37b23c1f5a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-callr@3.7:", type=("build", "run"))
	depends_on("r-fs@1.2.7:", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-git2r@0.26:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httpuv@1.2.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-knitr@1.29:", type=("build", "run"))
	depends_on("r-rmarkdown@1.18:", type=("build", "run"))
	depends_on("r-rprojroot@1.2:", type=("build", "run"))
	depends_on("r-rstudioapi@0.6:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-whisker@0.3.2:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
