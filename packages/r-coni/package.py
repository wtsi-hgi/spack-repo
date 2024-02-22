# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConi(RPackage):
	"""Correlation Guided Network Integration (CoNI)

	Integrates two numerical omics data sets from the same samples using partial correlations. The output can be represented as a network, bipartite graph or a hypergraph structure. The method used in the package refers to Klaus et al (2021) <doi:10.1016/j.molmet.2021.101295>.
	"""
	
	cran = "CoNI" 

	version("0.1.0", md5="63c45cce778dd312e2210cf30b4c5c25")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph@1.2.6:", type=("build", "run"))
	depends_on("r-doparallel@1.0.16:", type=("build", "run"))
	depends_on("r-cocor@1.1.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-forcats@0.5.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-data-table@1.13.7:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-genefilter@1.72.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.9.1:", type=("build", "run"))
	depends_on("r-gplots@3.1.1:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-ppcor@1.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-hmisc@4.4.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("python@3:", type=("build", "link", "run"))
