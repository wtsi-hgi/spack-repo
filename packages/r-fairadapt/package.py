# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFairadapt(RPackage):
	"""Fair Data Adaptation with Quantile Preservation

	An implementation of the fair data adaptation with quantile
    preservation described in Plecko & Meinshausen (2019) <arXiv:1911.06685>.
    The adaptation procedure uses the specified causal graph to pre-process the
    given training and testing data in such a way to remove the bias caused by
    the protected attribute. The procedure uses tree ensembles for quantile
    regression.
	"""
	
	homepage = "https://github.com/dplecko/fairadapt"
	cran = "fairadapt" 

	version("0.2.7", md5="b6f160249d94e0ded5c58fe5d648d176")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ranger@0.13.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-qrnn", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
