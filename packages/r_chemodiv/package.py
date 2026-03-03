# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemodiv(RPackage):
	"""Analysing Chemodiversity of Phytochemical Data

	Quantify and visualise various measures of chemical diversity and
    dissimilarity, for phytochemical compounds and other sets of chemical
    composition data. Importantly, these measures can incorporate biosynthetic
    and/or structural properties of the chemical compounds, resulting in a more
    comprehensive quantification of diversity and dissimilarity. For details,
    see Petrén, Köllner and Junker (2023) <doi:10.1111/nph.18685>.
	"""
	
	homepage = "https://github.com/hpetren/chemodiv"
	cran = "chemodiv" 

	version("0.3.0", md5="143f39442106404bbee6023f279cb404")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-webchem", type=("build", "run"))
	depends_on("r-fmcsr", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
	depends_on("r-hillr", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-gunifrac", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
