# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAiuq(RPackage):
	"""Ab Initio Uncertainty Quantification

	Uncertainty quantification and inverse estimation by probabilistic generative models  from the beginning of the data analysis. An example is a Fourier basis method for inverse estimation in scattering analysis of microscopy videos. It does not require specifying a certain range of Fourier bases and it substantially reduces computational cost via the generalized Schur algorithm. See the reference: Mengyang Gu, Yue He, Xubo Liu and Yimin Luo (2023), <arXiv:2309.02468>.
	"""
	
	cran = "AIUQ" 

	version("0.5.1", md5="5953d092c3fa52ca244fb58d2965d074")

	depends_on("r-fftwtools@0.9.11:", type=("build", "run"))
	depends_on("r-supergauss@2.0.3:", type=("build", "run"))
	depends_on("r-plot3d@1.4:", type=("build", "run"))
