# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmlmkalman(RPackage):
	"""Generation and Tracking of Super-Resolution Filamentous Datasets

	A pair of functions that allow for the generation and tracking of coordinate data clouds without a time dimension,
    primarily for use in super-resolution plant micro-tubule image segmentation.
	"""
	
	cran = "smlmkalman" 

	version("0.1.1", md5="26088da22de78ded1535d5eb9fcdd924")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
