# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdma(RPackage):
	"""Dynamic Model Averaging and Dynamic Model Selection for
Continuous Outcomes

	Allows to estimate dynamic model averaging, dynamic model selection and median probability model. The original methods are implemented, as well as, selected further modifications of these methods. In particular the user might choose between recursive moment estimation and exponentially moving average for variance updating. Inclusion probabilities might be modified in a way using 'Google Trends'. The code is written in a way which minimises the computational burden (which is quite an obstacle for dynamic model averaging if many variables are used). For example, this package allows for parallel computations and Occam's window approach. The package is designed in a way that is hoped to be especially useful in economics and finance. Main reference: Raftery, A.E., Karny, M., Ettler, P. (2010) <doi:10.1198/TECH.2009.08104>. 
	"""
	
	homepage = "https://CRAN.R-project.org/package=fDMA"
	cran = "fDMA" 

	version("2.2.7", md5="0df60605c8853d9e64478f86806e4e32")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
