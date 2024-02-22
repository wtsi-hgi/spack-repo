# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCops(RPackage):
	"""Cluster Optimized Proximity Scaling

	Multidimensional scaling (MDS) methods that aim at pronouncing the clustered appearance of the configuration (Rusch, Mair & Hornik, 2021, <doi:10.1080/10618600.2020.1869027>). They achieve this by transforming proximities/distances with power functions and augment the fitting criterion with a clusteredness index, the OPTICS Cordillera (Rusch, Hornik & Mair, 2018, <doi:10.1080/10618600.2017.1349664>). There are two variants: One for finding the configuration directly (COPS-C) for ratio, power, interval and non-metric MDS (Borg & Groenen, 2005, ISBN:978-0-387-28981-6), and one for using the augmented fitting criterion to find optimal parameters (P-COPS). The package contains various functions, wrappers, methods and classes for fitting, plotting and displaying different MDS models in a COPS framework like ratio, interval and non-metric MDS for COPS-C and P-COPS with Torgerson scaling (Torgerson, 1958, ISBN:978-0471879459), scaling by majorizing a complex function (SMACOF; de Leeuw, 1977, <https://escholarship.org/uc/item/4ps3b5mj>), Sammon mapping (Sammon, 1969, <doi:10.1109/T-C.1969.222678>), elastic scaling (McGee, 1966, <doi:10.1111/j.2044-8317.1966.tb00367.x>), s-stress (Takane, Young & de Leeuw, 1977, <doi:10.1007/BF02293745>), r-stress (de Leeuw, Groenen & Mair, 2016, <https://rpubs.com/deleeuw/142619>), power stress (Buja & Swayne, 2002 <doi:10.1007/s00357-001-0031-0>), restricted power stress, approximate power stress, power elastic scaling, power Sammon mapping (for all Rusch, Mair & Hornik, 2021, <doi:10.1080/10618600.2020.1869027>). All of these models can also solely be fit as MDS with power transformations. The package further contains a function for pattern search optimization, the ``Adaptive Luus-Jaakola Algorithm'' (Rusch, Mair & Hornik, 2021,<doi:10.1080/10618600.2020.1869027>).
	"""
	
	homepage = "https://r-forge.r-project.org/projects/stops/"
	cran = "cops" 

	version("1.3-1", md5="a6a76662bded63faf1d63721650d4855")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-cordillera@0.7.2:", type=("build", "run"))
	depends_on("r-smacof@1.10.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-nlcoptim", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-subplex", type=("build", "run"))
	depends_on("r-cmaes", type=("build", "run"))
	depends_on("r-crs", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
