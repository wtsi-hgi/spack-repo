# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttr2(RPackage):
	"""Perform HTTP Requests and Process the Responses.

	Tools for creating and modifying HTTP requests, then performing them and
	processing the results. 'httr2' is a modern re-imagining of 'httr' that
	uses a pipe-based interface and solves more of the problems that API
	wrapping packages face."""

	cran = "httr2"
	version("0.2.2", sha256="5d1ab62541f7817112519f0f9d00d6a2555bab5b2da7f5c6d579b0c307d7f2bf")
	version("1.0.1", md5="3f2a80e58b643169eb65bed398105f18", url="https://cran.r-project.org/src/contrib/httr2_1.0.1.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-curl@5.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.6.3:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
