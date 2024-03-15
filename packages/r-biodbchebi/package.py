# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbchebi(RPackage):
	"""biodbChebi, a library for connecting to the ChEBI Database

	The biodbChebi library provides access to the ChEBI Database, using biodb package framework. It allows to retrieve entries by their accession number. Web services can be accessed for searching the database by name, mass or other fields.
	"""
	
	homepage = "https://github.com/pkrog/biodbChebi"
	bioc = "biodbChebi" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biodbChebi_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biodbChebi/biodbChebi_1.8.0.tar.gz"]

	version("1.8.0", md5="31f6ed155e1126b62c5a6cd7fbd6c742")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-biodb@1.1.5:", type=("build", "run"))
