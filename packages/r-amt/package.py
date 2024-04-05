# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmt(RPackage):
	"""Animal Movement Tools

	Manage and analyze animal movement data. The functionality of
    'amt' includes methods to calculate home ranges, track statistics
    (e.g. step lengths, speed, or turning angles), prepare data for
    fitting habitat selection analyses, and simulation of space-use from
    fitted step-selection functions.
	"""
	
	homepage = "https://github.com/jmsigner/amt"
	cran = "amt" 

	version("0.2.2.0", md5="03e9fbc432bb09b9302fc840aa2fc7e9")
	version("0.2.1.0", md5="721897f7390713213cd2442f50cc15cc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-ctmm", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
