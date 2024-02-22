# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROgi(RPackage):
	"""Objective General Index

	Consider a data matrix of n individuals with p variates. The objective general index (OGI)
    is a general index that combines the p variates into a univariate index in order to rank the n
    individuals. The OGI is always positively correlated with each of the variates.
    More details can be found in Sei (2016) <doi:10.1016/j.jmva.2016.02.005>.
	"""
	
	cran = "OGI" 

	version("1.0.0", md5="06cfe14348a4ef60748e521e99dc90f1")

	depends_on("r-lpsolve@5.6.13:", type=("build", "run"))
