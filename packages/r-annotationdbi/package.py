# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationdbi(RPackage):
	"""Manipulation of SQLite-based annotations in Bioconductor.

	Implements a user-friendly interface for querying SQLite-based
	annotation data packages."""

	bioc = "AnnotationDbi"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/AnnotationDbi_1.64.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/AnnotationDbi/AnnotationDbi_1.64.1.tar.gz"]

	version("1.64.1", md5="965300db0b7a8b527ed3eb00fdd6d10f")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-biocgenerics@0.29.2:", type=("build", "run"))
	depends_on("r-biobase@1.17:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
