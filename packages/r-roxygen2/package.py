# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoxygen2(RPackage):
	"""In-Line Documentation for R.

	Generate your Rd documentation, 'NAMESPACE' file, and collation field using
	specially formatted comments. Writing documentation in-line with code makes
	it easier to keep your documentation up-to-date as your requirements
	change. 'Roxygen2' is inspired by the 'Doxygen' system for C++."""

	cran = "roxygen2"

	version("7.3.1", md5="0889cc9894460b64931b8a2853994f7b", url="https://cran.r-project.org/src/contrib/roxygen2_7.3.1.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-commonmark", type=("build", "run"))
	depends_on("r-desc@1.2:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-pkgload@1.0.2:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-r6@2.1.2:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
