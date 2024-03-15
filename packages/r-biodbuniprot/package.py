# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbuniprot(RPackage):
	"""biodbUniprot, a library for connecting to the Uniprot Database

	The biodbUniprot library is an extension of the biodb framework package. It provides access to the UniProt database. It allows to retrieve entries by their accession number, and run web service queries for searching for entries.
	"""
	
	homepage = "https://github.com/pkrog/biodbUniprot"
	bioc = "biodbUniprot" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biodbUniprot_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biodbUniprot/biodbUniprot_1.8.0.tar.gz"]

	version("1.8.0", md5="f4f5bcc32018b6472836efcc8c82671c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-biodb@1.4.2:", type=("build", "run"))
