# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RRmarkdown(RPackage):
	"""Dynamic Documents for R.

	Convert R Markdown documents into a variety of formats."""

	cran = "rmarkdown"

	license("GPL-3.0-only")

	version("2.26", md5="d4f5e42ce1e7d2ab04fb1beff82c4ff5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bslib@0.2.5.1:", type=("build", "run"))
	depends_on("r-evaluate@0.13:", type=("build", "run"))
	depends_on("r-fontawesome@0.5:", type=("build", "run"))
	depends_on("r-htmltools@0.5.1:", type=("build", "run"))
	depends_on("r-jquerylib", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr@1.43:", type=("build", "run"))
	depends_on("r-tinytex@0.31:", type=("build", "run"))
	depends_on("r-xfun@0.36:", type=("build", "run"))
	depends_on("r-yaml@2.1.19:", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
