# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlgp(RPackage):
	"""Particle Learning of Gaussian Processes

	Sequential Monte Carlo (SMC) inference for fully Bayesian
  Gaussian process (GP) regression and classification models by
  particle learning (PL) following Gramacy & Polson (2011) <arXiv:0909.5262>.
  The sequential nature of inference
  and the active learning (AL) hooks provided facilitate thrifty 
  sequential design (by entropy) and optimization
  (by improvement) for classification and
  regression models, respectively.
  This package essentially provides a generic
  PL interface, and functions (arguments to the interface) which
  implement the GP models and AL heuristics.  Functions for 
  a special, linked, regression/classification GP model and 
  an integrated expected conditional improvement (IECI) statistic 
  provide for optimization in the presence of unknown constraints.
  Separable and isotropic Gaussian, and single-index correlation
  functions are supported.
  See the examples section of ?plgp and demo(package="plgp") 
  for an index of demos.
	"""
	
	homepage = "https://bobby.gramacy.com/r_packages/plgp/"
	cran = "plgp" 

	version("1.1-12", md5="7b00cea90a7e1bce0726b937047785ea")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tgp", type=("build", "run"))
