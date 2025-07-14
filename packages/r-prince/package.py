# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrince(RPackage):
	"""Predicting Interactomes from Co-Elution

	PrInCE (Predicting Interactomes from Co-Elution) uses a naive Bayes classifier trained on dataset-derived features to recover protein-protein interactions from co-elution chromatogram profiles. This package contains the R implementation of PrInCE.
	"""
	
	bioc = "PrInCE"

	version("1.24.0", commit="1d1ba2225ecbc5ef812f28a84dcdf1be77bc42bf")
	version("1.18.0", commit="9b7f847e4aac6c3b5791b31fd78adb95f3f87b72")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-tidyr@0.8.99:", type=("build", "run"))
	depends_on("r-forecast@8.2:", type=("build", "run"))
	depends_on("r-progress@1.1.2:", type=("build", "run"))
	depends_on("r-hmisc@4:", type=("build", "run"))
	depends_on("r-naivebayes@0.9.1:", type=("build", "run"))
	depends_on("r-robustbase@0.92.7:", type=("build", "run"))
	depends_on("r-ranger@0.8:", type=("build", "run"))
	depends_on("r-liblinear@2.10.8:", type=("build", "run"))
	depends_on("r-speedglm@0.3.2:", type=("build", "run"))
	depends_on("r-tester@0.1.7:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-biobase@2.40:", type=("build", "run"))
	depends_on("r-msnbase@2.8.3:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
