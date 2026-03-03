# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntsurv(RPackage):
	"""Integrative Survival Modeling

	Contains implementations of
    integrative survival analysis routines, including
    regular Cox cure rate model proposed by
    Kuk and Chen (1992) <doi:10.1093/biomet/79.3.531>
    via an EM algorithm proposed by
    Sy and Taylor (2000) <doi:10.1111/j.0006-341X.2000.00227.x>,
    regularized Cox cure rate model with elastic net penalty following
    Masud et al. (2018) <doi:10.1177/0962280216677748>, and
    Zou and Hastie (2005) <doi:10.1111/j.1467-9868.2005.00503.x>, and
    weighted concordance index for cure models proposed by
    Asano and Hirakawa (2017) <doi:10.1080/10543406.2017.1293082>.
	"""
	
	homepage = "https://wwenjie.org/intsurv"
	cran = "intsurv" 

	version("0.2.2", md5="5484b2a922aed7419af0862b6f99045f")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
