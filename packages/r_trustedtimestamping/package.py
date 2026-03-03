# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrustedtimestamping(RPackage):
	"""Create Trusted Timestamps of Datasets and Files

	Trusted Timestamps (tts) are created by incorporating a hash of a file or dataset into a transaction on the decentralized blockchain (Stellar network). 
    The package makes use of a free service provided by <https://stellarapi.io>.
	"""
	
	cran = "trustedtimestamping" 

	version("0.2.6", md5="afd025e7dfa1c4447028c79b4df146d5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
