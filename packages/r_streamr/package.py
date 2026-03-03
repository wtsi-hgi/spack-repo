# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStreamr(RPackage):
	"""Access to Twitter Streaming API via R

	Functions to access Twitter's filter, sample, and user streams, and to
    parse the output into data frames.
	"""
	
	cran = "streamR" 

	version("0.4.5", md5="db9f73f4e886cab40d04b95b8cff7c36")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-ndjson", type=("build", "run"))
