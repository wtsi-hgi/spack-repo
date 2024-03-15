# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReproducible(RPackage):
	"""A Set of Tools that Enhance Reproducibility Beyond Package Management.

	Collection of high-level, machine- and OS-independent tools for making
	deeply reproducible and reusable content in R. The two workhorse functions
	are Cache and prepInputs; these allow for: nested caching, robust to
	environments, and objects with environments (like functions); and data
	retrieval and processing in continuous workflow environments. In all cases,
	efforts are made to make the first and subsequent calls of functions have
	the same result, but vastly faster at subsequent times by way of checksums
	and digesting. Several features are still under active development,
	including cloud storage of cached objects, allowing for sharing between
	users. Several advanced options are available, see ?reproducibleOptions."""

	cran = "reproducible"

	maintainers("dorton21")

	license("GPL-3.0-only")

	version("2.0.10", md5="43839c228f065c7e8484095c42503ea8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
	depends_on("r-fpcompare", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-lobstr", type=("build", "run"))
	depends_on("unrar", type=("build", "link", "run"))
