# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoDb(RPackage):
	"""A set of annotation maps describing the entire Disease Ontology.

	A set of annotation maps describing the entire Disease
	Ontology assembled using data from DO."""

	# There is no git repository for this package.
	bioc = "DO.db"
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/DO.db_2.9.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/DO.db/DO.db_2.9.tar.gz"]
	
	version("2.9", sha256="762bcb9b5188274fd81d82f785cf2846a5acc61fad55e2ff8ec1502282c27881")
	version("2.9", md5="63dda6d46d2fe40c52a2e79260a7fb9d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

