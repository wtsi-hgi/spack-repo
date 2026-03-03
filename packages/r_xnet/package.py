# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXnet(RPackage):
	"""Two-Step Kernel Ridge Regression for Network Predictions

	Fit a two-step kernel ridge regression model for
        predicting edges in networks, and carry out cross-validation
        using shortcuts for swift and accurate performance assessment
        (Stock et al, 2018 <doi:10.1093/bib/bby095> ).
	"""
	
	homepage = "https://github.com/CenterForStatistics-UGent/xnet"
	cran = "xnet" 

	version("0.1.11", md5="f74889f63f4b89d7e8e9a4107911c342")

	depends_on("r@3.4:", type=("build", "run"))
