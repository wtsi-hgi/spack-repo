# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImfData(RPackage):
	"""An Interface to IMF (International Monetary Fund) Data JSON API

	A straightforward interface for accessing the IMF 
    (International Monetary Fund) data JSON API, 
    available at <https://data.imf.org/>. This package offers direct access to 
    the primary API endpoints: Dataflow, DataStructure, and CompactData. 
    And, it provides an intuitive interface for exploring available 
    dimensions and attributes, as well as querying individual time-series datasets. 
    Additionally, the package implements a rate limit on API calls to reduce the 
    chances of exceeding service limits (limited to 10 calls every 5 seconds) 
    and encountering response errors.
	"""
	
	homepage = "https://pedrobtz.github.io/imf.data/"
	cran = "imf.data" 

	version("0.1.4", md5="6827f6408a6a94de88196b01edc0f123")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
