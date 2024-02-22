# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestly(RPackage):
	"""Interactive Forest Plot

	Interactive forest plot for clinical trial safety analysis
    using 'metalite', 'reactable', 'plotly', and Analysis Data Model (ADaM)
    datasets. Includes functionality for adverse event filtering,
    incidence-based group filtering, hover-over reveals, and search and sort
    operations. The workflow allows for metadata construction, data preparation,
    output formatting, and interactive plot generation.
	"""
	
	cran = "forestly" 

	version("0.1.0", md5="fc6de288fbbf12ab4376c0b4ae6d4f66")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-metalite", type=("build", "run"))
	depends_on("r-metalite-ae", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
