# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocc(RPackage):
	"""ROC Based Classification

	Functions for a classification method based on receiver operating characteristics (ROC). Briefly, features are selected according to their ranked AUC value in the training set. The selected features are merged by the mean value to form a meta-gene. The samples are ranked by their meta-gene value and the meta-gene threshold that has the highest accuracy in splitting the training samples is determined. A new sample is classified by its meta-gene value relative to the threshold. In the first place, the package is aimed at two class problems in gene expression data, but might also apply to other problems.
	"""
	
	cran = "rocc" 

	version("1.3", md5="ff8fc631a378639a2af03ec8a6d07f86")

	depends_on("r-rocr", type=("build", "run"))
