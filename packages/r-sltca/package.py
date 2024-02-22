# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSltca(RPackage):
	"""Scalable and Robust Latent Trajectory Class Analysis

	Conduct latent trajectory class analysis with longitudinal data. Our method supports longitudinal continuous, binary and count data. For more methodological details, please refer to Hart, K.R., Fei, T. and Hanfelt, J.J. (2020), Scalable and robust latent trajectory class analysis using artificial likelihood. Biometrics <doi:10.1111/biom.13366>.
	"""
	
	cran = "SLTCA" 

	version("0.1.0", md5="67a90ef12529f4111a97c6f2a0440ea2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
