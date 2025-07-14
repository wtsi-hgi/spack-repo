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

	version("1.16.0", commit="e0ed11f96bb45bb0bcd75625476ea73ccbe88755")
	version("1.10.0", commit="576eb76d2e6e41870b8e399d70ee2ae86acc5a4e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
