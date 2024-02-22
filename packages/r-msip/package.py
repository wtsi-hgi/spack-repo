# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsip(RPackage):
	"""'MassSpectrometry' Interaction Prediction

	The 'MSiP' is a computational approach to predict protein-protein interactions from large-scale affinity purification mass 'spectrometry' (AP-MS) data. This approach includes both spoke and matrix models for interpreting AP-MS data in a network context. The "spoke" model considers only bait-prey interactions, whereas the "matrix" model assumes that each of the identified proteins (baits and prey) in a given AP-MS experiment interacts with each of the others. The spoke model has a high false-negative rate, whereas the matrix model has a high false-positive rate. Although, both statistical models have merits, a combination of both models has shown to increase the performance of machine learning classifiers in terms of their capabilities in discrimination between true and false positive interactions.
	"""
	
	cran = "MSiP" 

	version("1.3.7", md5="9c2f54f404a528f6bc0162975e24d0d7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-tibble@3.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-prroc@1.3.1:", type=("build", "run"))
	depends_on("r-caret@6.0.88:", type=("build", "run"))
	depends_on("r-e1071@1.7.7:", type=("build", "run"))
	depends_on("r-mice@3.13:", type=("build", "run"))
	depends_on("r-proc@1.17.0.1:", type=("build", "run"))
	depends_on("r-ranger@0.12.1:", type=("build", "run"))
