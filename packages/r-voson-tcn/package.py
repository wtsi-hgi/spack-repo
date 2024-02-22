# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVosonTcn(RPackage):
	"""Twitter Conversation Networks and Analysis

	Collects tweets and metadata for threaded conversations and
    generates networks.
	"""
	
	homepage = "https://github.com/vosonlab/voson.tcn"
	cran = "voson.tcn" 

	version("0.5.0", md5="ecadf923085b39413bff22c7ff3ca985")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
