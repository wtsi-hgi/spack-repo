# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeshdbi(RPackage):
	"""DBI to construct MeSH-related package from sqlite file

	The package is unified implementation of MeSH.db, MeSH.AOR.db, and MeSH.PCR.db and also is interface to construct Gene-MeSH package (MeSH.XXX.eg.db). loadMeSHDbiPkg import sqlite file and generate MeSH.XXX.eg.db.
	"""
	
	bioc = "MeSHDbi"

	version("1.44.0", commit="41619a445ce617e27c52b1ea7adb5af109dc8986")
	version("1.38.0", commit="7abf210085a5c22ce89137841fcef7c09b05062e")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-annotationdbi@1.31.19:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
