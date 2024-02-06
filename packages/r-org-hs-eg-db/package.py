# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgHsEgDb(RPackage):
	"""Genome wide annotation for Human.

	Genome wide annotation for Human, primarily based on mapping using Entrez
	Gene identifiers."""

	bioc = "org.Hs.eg.db"
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/org.Hs.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/org.Hs.eg.db/org.Hs.eg.db_3.18.0.tar.gz"]

	version("3.18.0", md5="e1f74b9d0c541b5678a0d88f6a8ec847")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation