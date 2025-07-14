# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCustomcmpdb(RPackage):
	"""Customize and Query Compound Annotation Database

	This package serves as a query interface for important community collections of small molecules, while also allowing users to include custom compound collections.
	"""
	
	homepage = "https://github.com/yduan004/customCMPdb/"
	bioc = "customCMPdb"

	version("1.18.0", commit="170349fc14b753fbb1f6823187e2b5229cb0bcf2")
	version("1.12.0", commit="b93db2fc13d04c50a11f152973c99d8c0cfdfb1f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
