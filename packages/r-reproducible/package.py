# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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
	version("1.2.16", sha256="ec504cdc1adf305cd008ce65eff226e3cb60b7a454b2c8b98a871c84458546ae")
	version("1.2.10", sha256="fcee3aeb9d38c561c95df8663614ff0ed91a871719730766171b4ed19c82f729")
	version("1.2.8", sha256="6f453016404f6a2a235cb4d951a29aa7394dc3bd0b9cfc338dc85fb3d5045dd5")
	version("1.2.4", sha256="0525deefa6a0713c3fe2da8bfc529f62d6352bebf2ef08866503b4853412f149")
	version("2.0.11", md5="3ac3168ed110a17272312b6efef8d6ba")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
	depends_on("r-fpcompare", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-lobstr", type=("build", "run"))
	depends_on("unrar", type=("build", "link", "run"))
