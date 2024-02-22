# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpscomps(RPackage):
	"""'systemPipeShiny' UI and Server Components

	The systemPipeShiny (SPS) framework comes with many UI and server components. However, installing the whole framework is heavy and takes some time. If you would like to use UI and server components from SPS in your own Shiny apps, do not hesitate to try this package.
	"""
	
	homepage = "https://github.com/lz100/spsComps"
	cran = "spsComps" 

	version("0.3.3.0", md5="5fbc9d095fd2df0dd62a2471fdff4ae4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shinytoastr", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
