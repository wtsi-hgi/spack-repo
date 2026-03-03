# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdataretriever(RPackage):
	"""R Interface to the Data Retriever

	Provides an R interface to the Data Retriever
    <https://retriever.readthedocs.io/en/latest/> via the Data Retriever's
    command line interface. The Data Retriever automates the
    tasks of finding, downloading, and cleaning public datasets,
    and then stores them in a local database.
	"""
	
	homepage = "https://docs.ropensci.org/rdataretriever/"
	cran = "rdataretriever" 

	version("3.1.0", md5="348c05055845e3e6c4b6f31939b827fc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-reticulate@1.16:", type=("build", "run"))
	depends_on("r-semver", type=("build", "run"))
	depends_on("python@3.7:", type=("build", "link", "run"))
