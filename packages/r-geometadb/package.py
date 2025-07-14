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

	version("1.70.0", commit="e0ebdde96df642854658763568c026de35179dea")
	version("1.64.0", commit="ca018f2324e0d81fcaa29765c5d493471d0c7a8f")

	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
