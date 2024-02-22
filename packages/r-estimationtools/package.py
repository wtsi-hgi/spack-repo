# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstimationtools(RPackage):
	"""Maximum Likelihood Estimation for Probability Functions from
Data Sets

	Total Time on Test plot and routines for parameter estimation of
    any lifetime distribution implemented in R via maximum likelihood (ML) given
    a data set. It is implemented thinking on parametric survival analysis, but
    it feasible to use in parameter estimation of probability density or mass
    functions in any field. The main routines 'maxlogL' and 'maxlogLreg' are
    wrapper functions specifically developed for ML estimation. There are
    included optimization procedures such as 'nlminb' and 'optim' from base
    package, and 'DEoptim' Mullen (2011) <doi: 10.18637/jss.v040.i06>. Standard
    errors are estimated with 'numDeriv' Gilbert (2011)
    <https://CRAN.R-project.org/package=numDeriv> or the option 'Hessian = TRUE'
    of 'optim' function.
	"""
	
	homepage = "https://jaimemosg.github.io/EstimationTools/"
	cran = "EstimationTools" 

	version("4.0.0", md5="455b947b7904095d39ad441afb292444")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-gaussquad", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-autoimage", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
