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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PrInCE_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PrInCE/PrInCE_1.18.0.tar.gz"]

	version("1.18.0", sha256="a6629b7d0779ac899df81d5a7db12b32c6955f9a3734e2e8f481f3366ccdfa63")

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
