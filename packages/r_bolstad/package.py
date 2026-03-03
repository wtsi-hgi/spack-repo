# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBolstad(RPackage):
	"""Functions for Elementary Bayesian Inference

	A set of R functions and data sets for the book Introduction to Bayesian Statistics, Bolstad, W.M. (2017), John Wiley & Sons ISBN 978-1-118-09156-2.
	"""
	
	cran = "Bolstad" 

	version("0.2-41", md5="21be529d72fc61c265982f56035b007e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
