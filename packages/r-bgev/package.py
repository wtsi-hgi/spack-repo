# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgev(RPackage):
	"""Bimodal GEV Distribution with Location Parameter

	Density, distribution function, quantile function random generation and estimation of bimodal GEV distribution given in Otiniano et al. (2023) <doi:10.1007/s10651-023-00566-7>. This new generalization of the well-known GEV (Generalized Extreme Value) distribution is useful for modeling heterogeneous bimodal data from different areas.
	"""
	
	cran = "bgev" 

	version("0.1", md5="e7e59b93a15a33ac2e77bdfa5236d8f3")

	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
