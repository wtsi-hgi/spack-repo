# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCggp(RPackage):
	"""Composite Grid Gaussian Processes

	Run computer experiments using the adaptive composite grid
    algorithm with a Gaussian process model.
    The algorithm works best when running an experiment that can evaluate thousands
    of points from a deterministic computer simulation.
    This package is an implementation of a forthcoming paper by Plumlee,
    Erickson, Ankenman, et al. For a preprint of the paper,
    contact the maintainer of this package.
	"""
	
	homepage = "https://github.com/CollinErickson/CGGP"
	cran = "CGGP" 

	version("1.0.4", md5="2d308079420cc607893c0640a3a32188")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
