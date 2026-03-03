# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocsvmPath(RPackage):
	"""The Entire Solution Paths for ROC-SVM

	We develop the entire solution paths for ROC-SVM presented by Rakotomamonjy. The ROC-SVM solution path algorithm greatly facilitates the tuning procedure for regularization parameter, lambda in ROC-SVM by avoiding grid search algorithm which may be computationally too intensive. For more information on the ROC-SVM, see the report in the ROC Analysis in AI workshop(ROCAI-2004) : Hernàndez-Orallo, José, et al. (2004) <doi:10.1145/1046456.1046489>.
	"""
	
	cran = "rocsvm.path" 

	version("0.1.0", md5="0bc88ff3f8547818276e96e936b3c6f9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-svmpath", type=("build", "run"))
