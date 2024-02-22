# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioimagedbs(RPackage):
	"""Bio- and biomedical imaging dataset for machine learning and deep learning (for ExperimentHub)

	The package provides a bioimage dataset for the image analysis using machine learning and deep learning. The dataset includes microscopy imaging data with supervised labels. The data is provided as R list data that can be loaded to Keras/tensorflow in R.
	"""
	
	homepage = "https://kumes.github.io/BioImageDbs/"
	bioc = "BioImageDbs" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/BioImageDbs_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/BioImageDbs/BioImageDbs_1.10.0.tar.gz"]

	version("1.10.0", md5="785e9ea81ef5699d70af969fd8d4703d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-filesstrings", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-einsum", type=("build", "run"))

	# experiment