# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasebasedreasoning(RPackage):
	"""Case Based Reasoning

	Case-based reasoning is a problem-solving methodology that involves solving a new problem by referring to the solution of a similar problem in a large set of previously solved problems. The key aspect of Case Based Reasoning is to determine the problem that "most closely" matches the new problem at hand. This is achieved by defining a family of distance functions and using these distance functions as parameters for local averaging regression estimates of the final result. The optimal distance function is chosen based on a specific error measure used in regression estimation. This approach allows for efficient problem-solving by leveraging past experiences and adapting solutions from similar cases. The underlying concept is inspired by the work of Dippon J. (2002) <doi:10.1016/S0167-9473(02)00058-0>.
	"""
	
	homepage = "https://github.com/sipemu/case-based-reasoning"
	cran = "CaseBasedReasoning" 

	version("0.3", md5="92d31543153aa459acd3ad190d47686a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
