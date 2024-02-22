# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpdbapi(RPackage):
	"""A Comprehensive Interface for Accessing the Protein Data Bank

	Streamlines the interaction with the RCSB Protein Data Bank (PDB) <https://www.rcsb.org/>. This interface offers an intuitive and 
            powerful tool for searching and retrieving a diverse range of data types from the PDB. It includes advanced functionalities like 
            BLAST and sequence motif queries. Built upon the existing XML-based API of the PDB, it simplifies the creation of custom requests, 
            thereby enhancing usability and flexibility for researchers.
	"""
	
	cran = "rPDBapi" 

	version("1.0", md5="c5855275c93d087f1d38d6bbf08e38c1")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-bio3d", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
