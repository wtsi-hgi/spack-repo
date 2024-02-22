# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarpack(RPackage):
	"""Solvers for Large Scale Eigenvalue and SVD Problems

	Previously an R wrapper of the 'ARPACK' library
    <http://www.caam.rice.edu/software/ARPACK/>, and now a shell of the
    R package 'RSpectra', an R interface to the 'Spectra' library
    <http://yixuan.cos.name/spectra/> for solving large scale
    eigenvalue/vector problems. The current version of 'rARPACK'
    simply imports and exports the functions provided by 'RSpectra'.
    New users of 'rARPACK' are advised to switch to the 'RSpectra' package.
	"""
	
	homepage = "https://github.com/yixuan/rARPACK"
	cran = "rARPACK" 

	version("0.11-0", md5="5dc8bf4f68ba4943d7aae306cc9ff68c")

	depends_on("r-rspectra", type=("build", "run"))
