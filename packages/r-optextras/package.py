# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptextras(RPackage):
	"""Tools to Support Optimization Possibly with Bounds and Masks

	Tools to assist in safely applying user generated objective and 
   derivative function to optimization programs. These are primarily function 
   minimization methods with at most bounds and masks on the parameters.
   Provides a way to check the basic computation of objective functions that 
   the user provides, along with proposed gradient and Hessian functions, 
   as well as to wrap such functions to avoid failures when inadmissible parameters 
   are provided. Check bounds and masks. Check scaling or optimality conditions. 
   Perform an axial search to seek lower points on the objective function surface. 
   Includes forward, central and backward gradient approximation codes.
	"""
	
	cran = "optextras" 

	version("2019-12.4", md5="fd03bbc4c2390d48216937e04f7cc026")

	depends_on("r-numderiv", type=("build", "run"))
