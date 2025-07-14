# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwitchde(RPackage):
	"""Switch-like differential expression across single-cell trajectories

	Inference and detection of switch-like differential expression across single-cell RNA-seq trajectories.
	"""
	
	homepage = "https://github.com/kieranrcampbell/switchde"
	bioc = "switchde" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/switchde_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/switchde/switchde_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="72ffe24b6d2eaac3bea44d205f8e9a862e18eac2f3ac6ccfbf816d7dba245370")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
