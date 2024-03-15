# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSampleclassifier(RPackage):
	"""Sample Classifier

	The package is designed to classify microarray RNA-seq gene expression profiles.
	"""
	
	bioc = "sampleClassifier" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sampleClassifier_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sampleClassifier/sampleClassifier_1.26.0.tar.gz"]

	version("1.26.0", md5="7f17cc7eb566dcd27148ee400491b6c7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mgfm", type=("build", "run"))
	depends_on("r-mgfr", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
