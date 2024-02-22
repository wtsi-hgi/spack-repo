# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbibutils(RPackage):
	"""Convert Between Bibliography Formats.

	Converts between a number of bibliography formats, including 'BibTeX',
	'BibLaTeX' and 'Bibentry'. Includes a port of the 'bibutils' utilities by
	Chris Putnam <https://sourceforge.net/projects/bibutils/>. Supports all
	bibliography formats and character encodings implemented in 'bibutils'."""

	cran = "rbibutils"

	version("2.2.16", md5="950c341d2b81351a3e194e460bd6870f")

	depends_on("r@2.10:", type=("build", "run"))
