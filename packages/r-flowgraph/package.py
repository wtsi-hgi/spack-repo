# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowgraph(RPackage):
	"""Identifying differential cell populations in flow cytometry data accounting for marker frequency

	Identifies maximal differential cell populations in flow cytometry data taking into account dependencies between cell populations; flowGraph calculates and plots SpecEnr abundance scores given cell population cell counts.
	"""
	
	homepage = "https://github.com/aya49/flowGraph"
	bioc = "flowGraph" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowGraph_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowGraph/flowGraph_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="df22e8d5cc64deaad2ad5ce74032ff9b05ecba187ee8570a817efc8d4bc856ea")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-effsize", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggiraph", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-data-table@1.9.5:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
