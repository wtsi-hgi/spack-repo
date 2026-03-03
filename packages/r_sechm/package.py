# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSechm(RPackage):
	"""sechm: Complex Heatmaps from a SummarizedExperiment

	sechm provides a simple interface between SummarizedExperiment objects and the ComplexHeatmap package. It enables plotting annotated heatmaps from SE objects, with easy access to rowData and colData columns, and implements a number of features to make the generation of heatmaps easier and more flexible. These functionalities used to be part of the SEtools package.
	"""
	
	bioc = "sechm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sechm_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sechm/sechm_1.10.0.tar.gz"]

	version("1.10.0", md5="6935a759779eaf70e1cbf3f22c7a1358")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
