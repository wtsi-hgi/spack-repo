# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBold(RPackage):
	"""Interface to Bold Systems API

	A programmatic interface to the Web Service methods provided by
    Bold Systems (<http://www.boldsystems.org/>) for genetic 'barcode' data.
    Functions include methods for searching by sequences by taxonomic names,
    ids, collectors, and institutions; as well as a function for searching
    for specimens, and downloading trace files.
	"""
	
	homepage = "https://docs.ropensci.org/bold/"
	cran = "bold" 

	version("1.3.0", sha256="4920fbebd22fb1d0f1a31ccc09c98aec446bb6cb5f65a2610437e405c0512c68")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-crul@0.3.8:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
