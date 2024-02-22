# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsdp(RPackage):
	"""Density Estimation with Semidefinite Programming

	The models of probability density functions are Gaussian or
    exponential distributions with polynomial correction terms.
    Using a maximum likelihood method, 'dsdp' computes parameters of Gaussian
    or exponential distributions together with degrees of polynomials by
    a grid search, and coefficient of polynomials by a variant of semidefinite
    programming. It adopts Akaike Information Criterion for model selection.
    See a vignette for a tutorial and more on our 'Github' repository 
    <https://github.com/tsuchiya-lab/dsdp/>.
	"""
	
	homepage = "https://tsuchiya-lab.github.io/dsdp/"
	cran = "dsdp" 

	version("0.1.1", md5="ab0737bccee0f28a9d4d7f6d39736c13")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
