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

    version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="e737bb5c078477ca0f38ba75b756c3c4f6db5ce39825687f7c6e4b074a46e061")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mgfm", type=("build", "run"))
	depends_on("r-mgfr", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
