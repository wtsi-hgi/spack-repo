# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdstim(RPackage):
	"""High Dimensional Stimulation Immune Mapping ('HDStIM')

	A method for identifying responses to experimental stimulation in mass or flow cytometry that uses high dimensional analysis of measured parameters and can be performed with an end-to-end unsupervised approach. In the context of in vitro stimulation assays where high-parameter cytometry was used to monitor intracellular response markers, using cell populations annotated either through automated clustering or manual gating for a combined set of stimulated and unstimulated samples, 'HDStIM' labels cells as responding or non-responding. The package also provides auxiliary functions to rank intracellular markers based on their contribution to identifying responses and generating diagnostic plots.
	"""
	
	homepage = "https://github.com/niaid/HDStIM"
	cran = "HDStIM" 

	version("0.1.0", md5="ee7332a53b92c8925ca82ba68d4f0de5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-boruta", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
