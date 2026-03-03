# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpinner(RPackage):
	"""An Implementation of Graph Net Architecture Based on 'torch'

	Proposes a 'torch' implementation of Graph Net architecture allowing different options for message passing and feature embedding.
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/spinner"
	cran = "spinner" 

	version("1.1.0", md5="f289653dcceda5cad19f2ad9321f8456")

	depends_on("r-torch@0.9:", type=("build", "run"))
	depends_on("r-igraph@1.3.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-ggthemes@4.2.4:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-readr@2.1.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-rlist@0.4.6.2:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
	depends_on("r-entropy@1.3.1:", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
