# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRollinglda(RPackage):
	"""Construct Consistent Time Series from Textual Data

	A rolling version of the Latent Dirichlet Allocation, see Rieger et al. (2021) <doi:10.18653/v1/2021.findings-emnlp.201>. By a sequential approach, it enables the construction of LDA-based time series of topics that are consistent with previous states of LDA models. After an initial modeling, updates can be computed efficiently, allowing for real-time monitoring and detection of events or structural breaks.
	"""
	
	homepage = "https://github.com/JonasRieger/rollinglda"
	cran = "rollinglda" 

	version("0.1.3", md5="33d422865dae0c2359e1281cd3ca9b25")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ldaprototype@0.3:", type=("build", "run"))
	depends_on("r-checkmate@1.8.5:", type=("build", "run"))
	depends_on("r-data-table@1.11.2:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tosca@0.2.0:", type=("build", "run"))
