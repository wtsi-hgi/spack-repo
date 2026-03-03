# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbflobr(RPackage):
	"""Read and Write Files to SQLite Databases

	Reads and writes files to SQLite databases
    <https://www.sqlite.org/index.html> as flobs (a flob is a blob that
    preserves the file extension).
	"""
	
	homepage = "https://github.com/poissonconsulting/dbflobr"
	cran = "dbflobr" 

	version("0.2.2", md5="2be6abe9dd3b294cb850f523bb1468d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-blob", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-flobr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
