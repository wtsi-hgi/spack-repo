# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmvarkit(RPackage):
	"""Estimate Gaussian and Student's t Mixture Vector Autoregressive
Models

	Unconstrained and constrained maximum likelihood estimation of structural and reduced form 
    Gaussian mixture vector autoregressive, Student's t mixture vector autoregressive, and Gaussian and Student's t
    mixture vector autoregressive models, quantile residual tests, graphical diagnostics,
    simulations, forecasting, and estimation of generalized impulse response function and generalized 
    forecast error variance decomposition.
    Leena Kalliovirta, Mika Meitz, Pentti Saikkonen (2016) <doi:10.1016/j.jeconom.2016.02.012>,
    Savi Virolainen (forthcoming) <doi:10.1080/07350015.2024.2322090>,
    Savi Virolainen (2022) <arXiv:2109.13648>.
	"""
	
	cran = "gmvarkit" 

	version("2.1.2", md5="c2a47c9258cb73f8b4cfa114abbf9c16")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-brobdingnag@1.2.4:", type=("build", "run"))
	depends_on("r-mvnfast@0.2.5:", type=("build", "run"))
	depends_on("r-pbapply@1.4.2:", type=("build", "run"))
	depends_on("r-gsl@2.1.6:", type=("build", "run"))
