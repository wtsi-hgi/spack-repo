# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothapc(RPackage):
	"""Smoothing of Two-Dimensional Demographic Data, Optionally Taking
into Account Period and Cohort Effects

	The implemented method uses for smoothing bivariate thin plate
    splines, bivariate lasso-type regularization, and allows for both period
    and cohort effects. Thus the mortality rates are modelled as the sum of four
    components: a smooth bivariate function of age and time, smooth one-dimensional
    cohort effects, smooth one-dimensional period effects and random errors.
	"""
	
	homepage = "https://bitbucket.org/alexanderdokumentov/smoothapcpackage"
	cran = "smoothAPC" 

	version("0.3", md5="ddbdb169e306c1f54d36aed643c103c9")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
