# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRereg(RPackage):
	"""Recurrent Event Regression

	A comprehensive collection of practical and easy-to-use tools for regression analysis of recurrent events, with or without the presence of a (possibly) informative terminal event described in Chiou et al. (2023) <doi:10.18637/jss.v105.i05>. The modeling framework is based on a joint frailty scale-change model, that includes models described in Wang et al. (2001) <doi:10.1198/016214501753209031>, Huang and Wang (2004) <doi:10.1198/016214504000001033>, Xu et al. (2017) <doi:10.1080/01621459.2016.1173557>, and Xu et al. (2019) <doi:10.5705/SS.202018.0224> as special cases. The implemented estimating procedure does not require any parametric assumption on the frailty distribution. The package also allows the users to specify different model forms for both the recurrent event process and the terminal event. 
	"""
	
	homepage = "https://github.com/stc04003/reReg"
	cran = "reReg" 

	version("1.4.6", md5="90a736d1666025cbf5019edfe1f406c1")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-directlabels", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reda@0.5:", type=("build", "run"))
	depends_on("r-scam", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
