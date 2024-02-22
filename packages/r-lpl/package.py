# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpl(RPackage):
	"""Local Partial Likelihood Estimation and Simultaneous Confidence
Band

	Local partial likelihood estimation by Fan, Lin and Zhou(2006)<doi:10.1214/009053605000000796> and simultaneous confidence band is a set of tools to test the covariates-biomarker interaction for survival data. Test for the covariates-biomarker interaction using the bootstrap method and the asymptotic method with simultaneous confidence band (Liu, Jiang and Chen (2015)<doi:10.1002/sim.6563>).
	"""
	
	cran = "lpl" 

	version("0.11", md5="f907614bf94d6f34fde335ce4b44bb8f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
