# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXmrr(RPackage):
	"""Generate XMR Control Chart Data from Time-Series Data

	XMRs combine X-Bar control charts and Moving Range control charts. These functions also will recalculate the reference lines when significant change has occurred. 
	"""
	
	cran = "xmrr" 

	version("1.1.1", md5="a1e2071f21c539d5ce5bcc355d6859f9")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
