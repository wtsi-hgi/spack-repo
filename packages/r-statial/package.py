# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatial(RPackage):
	"""A package to identify changes in cell state relative to spatial associations

	Statial is a suite of functions for identifying changes in cell state. The functionality provided by Statial provides robust quantification of cell type localisation which are invariant to changes in tissue structure. In addition to this Statial uncovers changes in marker expression associated with varying levels of localisation. These features can be used to explore how the structure and function of different cell types may be altered by the agents they are surrounded with.
	"""
	
	homepage = "https://sydneybiox.github.io/Statial"
	bioc = "Statial" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Statial_1.4.5.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Statial/Statial_1.4.5.tar.gz"]

	version("1.10.0", tag="RELEASE_3_21")
	version("1.4.5", sha256="b89442b4b517f18f08c3fc7052c16d17473a4b0c771bc3faba7787f6989d32c3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
