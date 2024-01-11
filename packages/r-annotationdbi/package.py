# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationdbi(RPackage):
	"""Manipulation of SQLite-based annotations in Bioconductor.

	Implements a user-friendly interface for querying SQLite-based
	annotation data packages."""

	bioc = "AnnotationDbi"

	version("1.64.0", commit="b613fce8a69ff4a9cd9b1b9bfff4758fe86cd9be")

	depends_on("r@2.7.0:", type=("build", "run"))
	depends_on("r-biocgenerics@0.29.2:", type=("build", "run"))
	depends_on("r-biobase@1.17.0:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))