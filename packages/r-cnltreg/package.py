# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnltreg(RPackage):
	"""Complex-Valued Wavelet Lifting for Signal Denoising

	Implementations of recent complex-valued wavelet shrinkage procedures for smoothing irregularly sampled signals, see Hamilton et al (2018) <doi:10.1080/00401706.2017.1281846>.
	"""
	
	cran = "CNLTreg" 

	version("0.1-2", md5="3fdffd3f017bc0ea73318d737c7f0423")

	depends_on("r-adlift", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-nlt", type=("build", "run"))
