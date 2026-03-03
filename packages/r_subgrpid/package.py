# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubgrpid(RPackage):
	"""Patient Subgroup Identification for Clinical Drug Development

	Implementation of Sequential BATTing (bootstrapping and aggregating of thresholds from trees) for developing threshold-based multivariate (prognostic/predictive) biomarker signatures. Variable selection is automatically built-in. Final signatures are returned with interaction plots for predictive signatures. Cross-validation performance evaluation and testing dataset results are also output. Detail algorithms are described in Huang et al (2017) <doi:10.1002/sim.7236>.
	"""
	
	cran = "SubgrpID" 

	version("0.12", md5="1aa054bb1ecbe22c07227c2a70e10d8e")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
