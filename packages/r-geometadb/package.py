# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeometadb(RPackage):
	"""A compilation of metadata from NCBI GEO

	The NCBI Gene Expression Omnibus (GEO) represents the largest public repository of microarray data. However, finding data of interest can be challenging using current tools. GEOmetadb is an attempt to make access to the metadata associated with samples, platforms, and datasets much more feasible. This is accomplished by parsing all the NCBI GEO metadata into a SQLite database that can be stored and queried locally. GEOmetadb is simply a thin wrapper around the SQLite database along with associated documentation. Finally, the SQLite database is updated regularly as new data is added to GEO and can be downloaded at will for the most up-to-date metadata. GEOmetadb paper: http://bioinformatics.oxfordjournals.org/cgi/content/short/24/23/2798 .
	"""
	
	bioc = "GEOmetadb" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GEOmetadb_1.64.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GEOmetadb/GEOmetadb_1.64.0.tar.gz"]

	version("1.64.0", md5="78e0bce3aa72836e1b126536221059c6")

	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
