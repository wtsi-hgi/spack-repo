# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendtwosub(RPackage):
	"""Two Sample Order Free Trend Nonparametric Inference

	Non-parametric trend comparison of two independent samples with sequential subsamples. For more details, please refer to Wang, Stapleton, and Chen (2018) <doi:10.1080/00949655.2018.1482492>. 
	"""
	
	cran = "Trendtwosub" 

	version("0.0.2", md5="d6873a84ed75c3ce8619c61474f208b2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
