# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtrlearn2(RPackage):
	"""Statistical Learning Methods for Optimizing Dynamic Treatment
Regimes

	We provide a comprehensive software to estimate general K-stage DTRs from SMARTs with Q-learning and a variety of outcome-weighted learning methods. Penalizations are allowed for variable selection and model regularization. With the outcome-weighted learning scheme, different loss functions - SVM hinge loss, SVM ramp loss, binomial deviance loss, and L2 loss - are adopted to solve the weighted classification problem at each stage; augmentation in the outcomes is allowed to improve efficiency. The estimated DTR can be easily applied to a new sample for individualized treatment recommendations or DTR evaluation.
	"""
	
	cran = "DTRlearn2" 

	version("1.1", md5="9d7d0faf4271afefbc0acc3a0ae8b525", url="https://cran.r-project.org/src/contrib/DTRlearn2_1.1.tar.gz")

	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
