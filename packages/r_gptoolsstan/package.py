# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGptoolsstan(RPackage):
	"""Gaussian Processes on Graphs and Lattices in 'Stan'

	Gaussian processes are flexible distributions to model functional data. Whilst
    theoretically appealing, they are computationally cumbersome except for small datasets.
    This package implements two methods for scaling Gaussian process inference in 'Stan'. First, a
    sparse approximation of the likelihood that is generally applicable and, second, an exact method
    for regularly spaced data modeled by stationary kernels using fast Fourier methods. Utility
    functions are provided to compile and fit 'Stan' models using the 'cmdstanr' interface.
    References: Hoffmann and Onnela (2022) <arXiv:2301.08836>.
	"""
	
	cran = "gptoolsStan" 

	version("0.1.0", md5="5a31a86b71d27a4802dbd92acd03a5ef")

