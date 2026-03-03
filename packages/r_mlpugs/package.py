# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlpugs(RPackage):
	"""Multi-Label Prediction Using Gibbs Sampling (and Classifier
Chains)

	An implementation of classifier chains (CC's) for multi-label
    prediction. Users can employ an external package (e.g. 'randomForest',
    'C50'), or supply their own. The package can train a single set of CC's or
    train an ensemble of CC's -- in parallel if running in a multi-core
    environment. New observations are classified using a Gibbs sampler since
    each unobserved label is conditioned on the others. The package includes
    methods for evaluating the predictions for accuracy and aggregating across
    iterations and models to produce binary or probabilistic classifications.
	"""
	
	homepage = "https://github.com/bearloga/MLPUGS"
	cran = "MLPUGS" 

	version("0.2.0", md5="3d609bcf5f2e63948545b5a0c5c42b21")

	depends_on("r@3.1.2:", type=("build", "run"))
