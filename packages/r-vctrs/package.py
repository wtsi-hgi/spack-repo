# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVctrs(RPackage):
	"""Vector Helpers.

	Defines new notions of prototype and size that are used to provide tools
	for consistent and well-founded type-coercion and size-recycling, and are
	in turn connected to ideas of type- and size-stability useful for analyzing
	function interfaces."""

	cran = "vctrs"

	version("0.6.5", md5="191f3037d9b6f3f8640661f61e2aeb93")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
