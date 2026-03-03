# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtmopt(RPackage):
	"""Analysis-of-Marginal-Tail-Means

	Provides functions for implementing the Analysis-of-marginal-Tail-Means (ATM) method, a robust optimization method for discrete black-box optimization. Technical details can be found in Mak and Wu (2018+) <arXiv:1712.03589>. This work was supported by USARO grant W911NF-17-1-0007.
	"""
	
	cran = "atmopt" 

	version("0.1.0", md5="c59bf020fdcb614303f2eecb4f9e719d")

	depends_on("r-doe-base", type=("build", "run"))
	depends_on("r-hiernet", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
