# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReservoirnet(RPackage):
	"""Reservoir Computing and Echo State Networks

	A simple user-friendly library based on the 'python' module 'reservoirpy'.
             It provides a flexible interface to implement efficient Reservoir
             Computing (RC) architectures with a particular focus on Echo State Networks
             (ESN). Some of its features are: offline and online training, parallel implementation, 
             sparse matrix computation, fast spectral initialization, advanced learning 
             rules (e.g. Intrinsic Plasticity) etc. It also makes possible to easily create 
             complex architectures with multiple reservoirs (e.g. deep reservoirs), readouts, 
             and complex feedback loops. Moreover, graphical tools are included to easily 
             explore hyperparameters. Finally, it includes several tutorials exploring
             time series forecasting, classification and hyperparameter tuning. For more information
             about 'reservoirpy', please see Trouvain et al. (2020) <doi:10.1007/978-3-030-61616-8_40>.
             This package was developed in the framework of the University of Bordeaux’s IdEx
             "Investments for the Future" program / RRI PHDS.
	"""
	
	homepage = "https://github.com/reservoirpy"
	cran = "reservoirnet" 

	version("0.2.0", md5="5c55a6be92d842bdada3630e2883d88a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("python@3.7:", type=("build", "link", "run"))
