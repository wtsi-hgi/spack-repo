# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesimages(RPackage):
	"""Bayesian Methods for Image Segmentation using a Potts Model

	Various algorithms for segmentation of 2D and 3D images, such
    as computed tomography and satellite remote sensing. This package implements
    Bayesian image analysis using the hidden Potts model with external field
    prior of Moores et al. (2015) <doi:10.1016/j.csda.2014.12.001>.
    Latent labels are sampled using chequerboard updating or Swendsen-Wang.
    Algorithms for the smoothing parameter include pseudolikelihood, path sampling,
    the exchange algorithm, approximate Bayesian computation (ABC-MCMC and ABC-SMC),
    and the parametric functional approximate Bayesian (PFAB) algorithm. Refer to
    <doi:10.1007/978-3-030-42553-1_6> for an overview and also to <doi:10.1007/s11222-014-9525-6>
    and <doi:10.1214/18-BA1130> for further details of specific algorithms.
	"""
	
	homepage = "https://bitbucket.org/Azeari/bayesimages"
	cran = "bayesImageS" 

	version("0.6-1", md5="ce0ee36d244cd9bb3910f49b2db8a401")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
