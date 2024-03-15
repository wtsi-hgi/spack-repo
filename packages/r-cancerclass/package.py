# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancerclass(RPackage):
	"""Development and validation of diagnostic tests from high-dimensional molecular data

	The classification protocol starts with a feature selection step and continues with nearest-centroid classification. The accurarcy of the predictor can be evaluated using training and test set validation, leave-one-out cross-validation or in a multiple random validation protocol. Methods for calculation and visualization of continuous prediction scores allow to balance sensitivity and specificity and define a cutoff value according to clinical requirements.
	"""
	
	bioc = "cancerclass" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cancerclass_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cancerclass/cancerclass_1.46.0.tar.gz"]

	version("1.46.0", md5="b2e5d6ec200ee08476480fa1f0a1577d")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
