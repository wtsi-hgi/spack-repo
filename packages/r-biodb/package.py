# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodb(RPackage):
	"""biodb, a library and a development framework for connecting to chemical and biological databases

	The biodb package provides access to standard remote chemical and biological databases (ChEBI, KEGG, HMDB, ...), as well as to in-house local database files (CSV, SQLite), with easy retrieval of entries, access to web services, search of compounds by mass and/or name, and mass spectra matching for LCMS and MSMS. Its architecture as a development framework facilitates the development of new database connectors for local projects or inside separate published packages.
	"""
	
	homepage = "https://github.com/pkrog/biodb"
	bioc = "biodb" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biodb_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biodb/biodb_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="73a5965ebaa6831b752ccc46abe4e8a200028d8de9a8a40cd5b1710eb43080a3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
