# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcollectl(RPackage):
	"""Help use collectl with R in Linux, to measure resource consumption in R processes

	Provide functions to obtain instrumentation data on processes in a unix environment.  Parse output of a collectl run.  Vizualize aspects of system usage over time, with annotation.
	"""
	
	homepage = "https://github.com/vjcitn/Rcollectl"
	bioc = "Rcollectl" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rcollectl_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rcollectl/Rcollectl_1.2.0.tar.gz"]

	version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="15b79b1c63e19a4966b8335849575a17ea5a13d1ed14520812aaa542d60da5ec")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
