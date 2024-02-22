# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmltools(RPackage):
	"""Tools for HTML.

	Tools for HTML generation and output."""

	cran = "htmltools"

	version("0.5.7", md5="3c644008d5b8c8dd01bedfda0d8a6527")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-fastmap@1.1:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
