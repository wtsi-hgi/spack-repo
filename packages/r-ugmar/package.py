# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUgmar(RPackage):
	"""Estimate Univariate Gaussian and Student's t Mixture
Autoregressive Models

	Maximum likelihood estimation of univariate Gaussian Mixture Autoregressive (GMAR),
    Student's t Mixture Autoregressive (StMAR), and Gaussian and Student's t Mixture Autoregressive (G-StMAR) models, 
    quantile residual tests, graphical diagnostics, forecast and simulate from GMAR, StMAR and G-StMAR processes. 
    Leena Kalliovirta, Mika Meitz, Pentti Saikkonen (2015) <doi:10.1111/jtsa.12108>, 
    Mika Meitz, Daniel Preve, Pentti Saikkonen (2023) <doi:10.1080/03610926.2021.1916531>,
    Savi Virolainen (2022) <doi:10.1515/snde-2020-0060>.
	"""
	
	cran = "uGMAR" 

	version("3.4.5", md5="8edeecce4db8833e303ef65e63e6ca95")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-brobdingnag@1.2.4:", type=("build", "run"))
	depends_on("r-pbapply@1.3.2:", type=("build", "run"))
	depends_on("r-gsl@1.9.10.3:", type=("build", "run"))
