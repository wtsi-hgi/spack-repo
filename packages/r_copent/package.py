# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopent(RPackage):
	"""Estimating Copula Entropy and Transfer Entropy

	The nonparametric methods for estimating copula entropy, transfer entropy, and the statistics for multivariate normality test and two-sample test are implemented. The methods for estimating transfer entropy and the statistics for multivariate normality test and two-sample test are based on the method for estimating copula entropy. Please refer to Ma and Sun (2011) <doi:10.1016/S1007-0214(11)70008-6>, Ma (2019) <arXiv:1910.04375>, Ma (2022) <arXiv:2206.05956>, and Ma (2023) <arXiv:2307.07247> for more information.
	"""
	
	homepage = "https://github.com/majianthu/copent"
	cran = "copent" 

	version("0.4", md5="145f34f568b8637d1f992bdb78f218fe")

	depends_on("r@2.7:", type=("build", "run"))
