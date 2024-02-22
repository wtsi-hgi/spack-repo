# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIc10trainingdata(RPackage):
	"""Training Datasets for iC10 Package

	Training datasets for iC10; which implements the classifier described in the paper 'Genome-driven integrated classification of breast cancer validated in over 7,500 samples' (Ali HR et al., Genome Biology 2014). It uses copy number and/or expression form breast cancer data, trains a pamr classifier (Tibshirani et al.) with the features available and predicts the iC10 group. Genomic annotation for the training dataset has been obtained from Mark Dunning's lluminaHumanv3.db package.
	"""
	
	cran = "iC10TrainingData" 

	version("1.3.1", md5="077ad100c88732bdefae178f52d9074a")

