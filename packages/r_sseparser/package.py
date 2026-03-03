# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSseparser(RPackage):
	"""Parse Server-Sent Events

	Functionality to parse server-sent events with a high-level
    interface that can be extended for custom applications.
	"""
	
	homepage = "https://github.com/calderonsamuel/SSEparser"
	cran = "SSEparser" 

	version("0.1.0", md5="ee7b0d98214dfebb3380694bb9bc3214")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
