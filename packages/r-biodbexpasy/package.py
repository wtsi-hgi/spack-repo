# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbexpasy(RPackage):
	"""biodbExpasy, a library for connecting to Expasy ENZYME database.

	The biodbExpasy library provides access to Expasy ENZYME database, using biodb package framework.  It allows to retrieve entries by their accession number. Web services can be accessed for searching the database by name or comments.
	"""
	
	bioc = "biodbExpasy"

	version("1.6.0", commit="abe7f9279fc51574bbe723e837ee669d44e5c425")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biodb@1.3.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
