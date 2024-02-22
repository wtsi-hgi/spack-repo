# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIc10(RPackage):
	"""A Copy Number and Expression-Based Classifier for Breast Tumours

	Implementation of the classifier described in the paper 'Genome-driven integrated classification of breast cancer validated in over 7,500 samples' (Ali HR et al., Genome Biology 2014). It uses copy number and/or expression form breast cancer data, trains a pamr classifier (Tibshirani et al.) with the features available and predicts the iC10 group.
	"""
	
	cran = "iC10" 

	version("1.5", md5="90248cbd2eb992ff818b02820db3dc7d", url="https://cran.r-project.org/src/contrib/iC10_1.5.tar.gz")

	depends_on("r-pamr", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-ic10trainingdata", type=("build", "run"))
