# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTricycle(RPackage):
	"""tricycle: Transferable Representation and Inference of cell cycle

	The package contains functions to infer and visualize cell cycle process using Single Cell RNASeq data. It exploits the idea of transfer learning, projecting new data to the previous learned biologically interpretable space. We provide a pre-learned cell cycle space, which could be used to infer cell cycle time of human and mouse single cell samples. In addition, we also offer functions to visualize cell cycle time on different embeddings and functions to build new reference.
	"""
	
	homepage = "https://github.com/hansenlab/tricycle"
	bioc = "tricycle" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tricycle_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tricycle/tricycle_1.10.0.tar.gz"]

	version("1.10.0", md5="6a6a35c0a2cd9f279395e046b98a79f6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scattermore", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
