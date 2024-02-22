# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsethis(RPackage):
	"""Automate Package and Project Setup.

	Automate package and project setup tasks that are otherwise performed
	manually. This includes setting up unit testing, test coverage, continuous
	integration, Git, 'GitHub', licenses, 'Rcpp', 'RStudio' projects, and
	more."""

	cran = "usethis"

	version("2.2.3", md5="e3890f0872a2222d7ee8b30dfe7473e4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.0.1:", type=("build", "run"))
	depends_on("r-clipr@0.3:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-curl@2.7:", type=("build", "run"))
	depends_on("r-desc@1.4.2:", type=("build", "run"))
	depends_on("r-fs@1.3:", type=("build", "run"))
	depends_on("r-gert@1.4.1:", type=("build", "run"))
	depends_on("r-gh@1.2.1:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-rprojroot@1.2:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-withr@2.3:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
