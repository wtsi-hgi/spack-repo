# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSequential(RPackage):
	"""Exact Sequential Analysis for Poisson and Binomial Data

	Functions to calculate exact critical values, statistical power, expected time to signal, and required sample sizes for performing exact sequential analysis. All these	calculations can be done for either Poisson or binomial data, for continuous or group sequential analyses, and for different types of rejection boundaries. In case of group sequential analyses, the group sizes do not have to be specified in advance and the alpha spending can be arbitrarily settled.
	"""
	
	cran = "Sequential" 

	version("4.3.3", md5="cc2393536006d7a5b71b7b8c0b9aeed9")

	depends_on("r-boot", type=("build", "run"))
