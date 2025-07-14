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

	version("1.32.0", commit="bfa7ffd2a86a77e07c86afb19998018cd29b3ce9")
	version("1.26.0", commit="eeda7c97001376edab5b0247df39d4caac4761f8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mgfm", type=("build", "run"))
	depends_on("r-mgfr", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
