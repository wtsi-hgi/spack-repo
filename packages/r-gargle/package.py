# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGargle(RPackage):
	"""Utilities for Working with Google APIs.

	Provides utilities for working with Google APIs
	<https://developers.google.com/apis-explorer>. This includes functions and
	classes for handling common credential types and for preparing, executing,
	and processing HTTP requests."""

	cran = "gargle"

	version("1.5.2", md5="d18b3d01e31e0dd4f4482aed5b85dc9c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.0.1:", type=("build", "run"))
	depends_on("r-fs@1.3.1:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-httr@1.4.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
