# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMousethymusageing(RPackage):
	"""Single-cell Transcriptomics Data of the Ageing Mouse Thymus

	This package provides data access to counts matrices and meta-data for single-cell RNA sequencing data of thymic epithlial cells across mouse ageing using SMARTseq2 and 10X Genommics chemistries. Access is provided as a data package via ExperimentHub. It is designed to facilitate the re-use of data from Baran-Gale _et al._ in a consistent format that includes relevant and informative meta-data.
	"""
	
	bioc = "MouseThymusAgeing" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MouseThymusAgeing_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MouseThymusAgeing/MouseThymusAgeing_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="1eccd42a2b8fccbd00d4c6ecc53dd01af3277e412bd2198028df17532650e7a6")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

