# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoDb(RPackage):
	"""A set of annotation maps describing the entire Gene Ontology.

	A set of annotation maps describing the entire Gene
	Ontology assembled using data from GO."""

	bioc = "GO.db"
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/GO.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/GO.db/GO.db_3.18.0.tar.gz"]

	version("3.18.0", md5="b23522167263afc45a9b115d01632cb1")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation