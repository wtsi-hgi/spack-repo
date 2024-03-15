# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogledrive(RPackage):
	"""An Interface to Google Drive.

	Manage Google Drive files from R."""

	cran = "googledrive"

	license("MIT")

	version("2.1.1", md5="2741deb58d88bacd81489316df7cf9e2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-gargle@1.5:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pillar@1.9:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
