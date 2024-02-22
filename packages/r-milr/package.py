# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMilr(RPackage):
	"""Multiple-Instance Logistic Regression with LASSO Penalty

	The multiple instance data set consists of many independent
    subjects (called bags) and each subject is composed of several components
    (called instances). The outcomes of such data set are binary or categorical responses,
    and, we can only observe the subject-level outcomes. For example, in manufacturing
    processes, a subject is labeled as "defective" if at least one of its own
    components is defective, and otherwise, is labeled as "non-defective". The
    'milr' package focuses on the predictive model for the multiple instance
    data set with binary outcomes and performs the maximum likelihood estimation
    with the Expectation-Maximization algorithm under the framework of logistic
    regression. Moreover, the LASSO penalty is attached to the likelihood function
    for simultaneous parameter estimation and variable selection.
	"""
	
	homepage = "https://github.com/PingYangChen/milr"
	cran = "milr" 

	version("0.3.1", md5="6d9b92535e34a9c2cd79eb48cc741310")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-piper@0.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
