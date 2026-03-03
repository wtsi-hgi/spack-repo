# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmradio(RPackage):
	"""Factor Modeling for Radiomics Data

	Functions that support stable prediction and classification with radiomics data through factor-analytic modeling. For details, see Peeters et al. (2019) <arXiv:1903.11696>.
	"""
	
	homepage = "https://github.com/CFWP/FMradio"
	cran = "FMradio" 

	version("1.1.1", md5="85312b40ce969cd927f589d7bc5cf00f")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
