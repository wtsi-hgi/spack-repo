# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdryad(RPackage):
	"""Access for Dryad Web Services

	Interface to the Dryad "Solr" API, their "OAI-PMH" service, and
    fetch datasets. Dryad (<https://datadryad.org/>) is a curated host of
    data underlying scientific publications.
	"""
	
	homepage = "https://docs.ropensci.org/rdryad"
	cran = "rdryad" 

	version("1.0.0", md5="c326aaf8f4b13b6946f0da13338c531c")

	depends_on("r-crul", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-hoardr", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
