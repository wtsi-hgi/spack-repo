# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpooky(RPackage):
	"""Time Feature Extrapolation Using Spectral Analysis and
Jack-Knife Resampling

	Proposes application of spectral analysis and jack-knife resampling for multivariate sequence forecasting. The application allows for a fast random search in a compact space of hyper-parameters composed by Sequence Length and Jack-Knife Leave-N-Out.
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/spooky"
	cran = "spooky" 

	version("1.4.0", md5="b73edd99aae078ec9776ea60cbb67628")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-readr@2.1.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-imputets@3.2:", type=("build", "run"))
	depends_on("r-fancova@0.6.1:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-modeest@2.4:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-greybox@1.0.1:", type=("build", "run"))
	depends_on("r-philentropy@0.5:", type=("build", "run"))
	depends_on("r-entropy@1.3.1:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
