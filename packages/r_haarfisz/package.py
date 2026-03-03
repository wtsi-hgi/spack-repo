# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHaarfisz(RPackage):
	"""Software to Perform Haar Fisz Transforms

	A Haar-Fisz algorithm for Poisson intensity estimation.
	Will denoise Poisson distributed sequences where
        underlying intensity is not constant. Uses the multiscale
        variance-stabilization method called the Haar-Fisz transform.
        Contains functions to carry out the forward and inverse
        Haar-Fisz transform and denoising on near-Gaussian sequences.
        Can also carry out cycle-spinning.
	Main reference: Fryzlewicz, P. and Nason, G.P. (2004)
	"A Haar-Fisz algorithm for Poisson intensity estimation."
        Journal of Computational and Graphical Statistics,
        13, 621-638. <doi:10.1198/106186004X2697>.
	"""
	
	cran = "haarfisz" 

	version("4.5.4", md5="21d796444c56a87802130a10db4bc0f8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
