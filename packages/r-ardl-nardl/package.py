# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArdlNardl(RPackage):
	"""Linear and Nonlinear Autoregressive Distributed Lag Models:
General-to-Specific Approach

	Estimate the linear and nonlinear autoregressive distributed lag (ARDL & NARDL) models and the corresponding error correction models, and test for longrun and short-run asymmetric. The general-to-specific approach is also available in estimating the ARDL and NARDL models. The Pesaran, Shin & Smith (2001) (<doi:10.1002/jae.616>) bounds test for level relationships is also provided. The 'ardl.nardl' package also performs short-run and longrun symmetric restrictions available at Shin et al. (2014) <doi:10.1007/978-1-4899-8008-3_9> and their corresponding tests.
	"""
	
	cran = "ardl.nardl" 

	version("1.3.0", md5="5bd83ca7e35499311ec237719b774bb2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gets", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-nardl", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
