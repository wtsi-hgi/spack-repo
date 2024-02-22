# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDde(RPackage):
	"""Solve Delay Differential Equations

	Solves ordinary and delay differential equations, where
    the objective function is written in either R or C.  Suitable only
    for non-stiff equations, the solver uses a 'Dormand-Prince' method
    that allows interpolation of the solution at any point.  This
    approach is as described by Hairer, Norsett and Wanner (1993)
    <ISBN:3540604529>.  Support is also included for iterating
    difference equations.
	"""
	
	homepage = "https://github.com/mrc-ide/dde"
	cran = "dde" 

	version("1.0.5", md5="ec31735c80d9cdf5ec081b41d743801c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ring@1:", type=("build", "run"))
