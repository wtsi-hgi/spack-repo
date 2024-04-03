# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmulator(RPackage):
	"""Bayesian Emulation of Computer Programs

	
 Allows one to estimate the output of a computer program,
 as a function of the input parameters, without actually running it.
 The computer program is assumed to be a Gaussian process, whose
 parameters are estimated using Bayesian techniques that give a PDF of
 expected program output.  This PDF is conditional on a training set
 of runs, each consisting of a point in parameter space and the model
 output at that point.  The emphasis is on complex codes that take
 weeks or months to run, and that have a large number of undetermined
 input parameters; many climate prediction models fall into this
 class.  The emulator essentially determines Bayesian posterior
 estimates of the PDF of the output of a model, conditioned on results
 from previous runs and a user-specified prior linear model.  The
 package includes functionality to evaluate quadratic forms 
 efficiently. 
	"""
	
	homepage = "https://github.com/RobinHankin/emulator"
	cran = "emulator" 

	version("1.2-21", md5="7c752262d3c1bac2bea21b4030292c44")
	version("1.2-24", md5="4b5e7598780b3dfa95c757427fbc198e")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
