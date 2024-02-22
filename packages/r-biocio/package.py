# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocio(RPackage):
	"""Standard Input and Output for Bioconductor Packages.

	Implements `import()` and `export()` standard generics for importing and
	exporting biological data formats. `import()` supports whole-file as well
	as chunk-wise iterative import. The `import()` interface optionally
	provides a standard mechanism for 'lazy' access via `filter()` (on row or
	element-like components of the file resource), `select()` (on column-like
	components of the file resource) and `collect()`. The `import()` interface
	optionally provides transparent access to remote (e.g. via https) as well
	as local access. Developers can register a file extension, e.g., `.loom`
	for dispatch from character-based URIs to specific `import()` / `export()`
	methods based on classes representing file types, e.g., `LoomFile()`."""

	bioc = "BiocIO"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BiocIO_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BiocIO/BiocIO_1.12.0.tar.gz"]

	version("1.12.0", md5="6e0c18bdf6d9f707f9d1e431400fa1c7")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
