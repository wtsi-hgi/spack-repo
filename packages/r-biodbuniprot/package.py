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

	version("1.14.0", commit="9bc6bb0d5a1e140c037238663f369ecf221e8930")
	version("1.8.0", commit="7b6e6b7960f233adfc836c807c0c44b25acaa013")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-biodb@1.4.2:", type=("build", "run"))
