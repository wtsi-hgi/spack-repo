# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeip(RPackage):
	"""Geophysical Inverse Theory and Optimization

	Several functions introduced in Aster et al.'s book on inverse theory. The functions are often translations of MATLAB code developed by the authors to illustrate concepts of inverse theory as applied to geophysics. Generalized inversion, tomographic inversion algorithms (conjugate gradients, 'ART' and 'SIRT'), non-linear least squares, first and second order Tikhonov regularization, roughness constraints, and procedures for estimating smoothing parameters are included. 
	"""
	
	cran = "PEIP" 

	version("2.2-5", md5="380033c59db8b0880e8f9f74d5647807")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-bvls", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rseis", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
