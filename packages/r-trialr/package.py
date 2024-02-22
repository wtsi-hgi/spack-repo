# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrialr(RPackage):
	"""Clinical Trial Designs in 'rstan'

	A collection of clinical trial designs and methods, implemented in 
    'rstan' and R, including: the Continual Reassessment Method by O'Quigley et 
    al. (1990) <doi:10.2307/2531628>; EffTox by Thall & Cook (2004) 
    <doi:10.1111/j.0006-341X.2004.00218.x>; the two-parameter logistic method of
    Neuenschwander, Branson & Sponer (2008) <doi:10.1002/sim.3230>; and the 
    Augmented Binary method by Wason & Seaman (2013) <doi:10.1002/sim.5867>; and
    more. We provide functions to aid model-fitting and analysis. 
    The 'rstan' implementations may also serve as a cookbook to anyone looking 
    to extend or embellish these models. We hope that this package encourages 
    the use of Bayesian methods in clinical trials. There is a preponderance of 
    early phase trial designs because this is where Bayesian methods are used 
    most. If there is a method you would like implemented, please get in touch.
	"""
	
	homepage = "https://github.com/brockk/trialr"
	cran = "trialr" 

	version("0.1.6", md5="33946b67cdd68a78563ab404002f22d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@1.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.2:", type=("build", "run"))
	depends_on("r-rstantools@1.5.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-tidybayes@2.0.3:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stanheaders@2.18.1:", type=("build", "run"))
	depends_on("r-bh@1.69.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.5:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.2:", type=("build", "run"))
