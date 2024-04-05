# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgdown(RPackage):
	"""Make Static HTML Documentation for a Package.

	Generate an attractive and useful website from a source package. 'pkgdown'
	converts your documentation, vignettes, 'README', and more to 'HTML' making
	it easy to share information about your package online."""

	cran = "pkgdown"
	version("2.0.7", sha256="f33872869dfa8319182d87e90eab3245ff69293b3b791471bf9538afb81b356a")
	version("2.0.7", md5="921aa30f4ce3f89b4ab9f5a41e41562a")
	version("2.0.6", sha256="d29a65c8a5b189fd89842e769f58f8c2369a55406269eabfb66d41d0fe1c7f69")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-bslib@0.3.1:", type=("build", "run"))
	depends_on("r-callr@3.7.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-downlit@0.4:", type=("build", "run"))
	depends_on("r-fs@1.4:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ragg", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-rmarkdown@1.1.9007:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-withr@2.4.3:", type=("build", "run"))
	depends_on("r-xml2@1.3.1:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
