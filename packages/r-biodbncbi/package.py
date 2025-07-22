# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbncbi(RPackage):
	"""biodbNcbi, a library for connecting to NCBI Databases.

	The biodbNcbi library provides access to the NCBI databases CCDS, Gene, Pubchem Comp and Pubchem Subst, using biodb package framework. It allows to retrieve entries by their accession number. Web services can be accessed for searching the database by name or mass.
	"""
	
	homepage = "https://github.com/pkrog/biodbNcbi"
	bioc = "biodbNcbi" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biodbNcbi_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biodbNcbi/biodbNcbi_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="859de0395db8acf97e2495cf269d7fece95054005ba3a3dcc69f1b19d0bc6ce2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biodb@1.3.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
