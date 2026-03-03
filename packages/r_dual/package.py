# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDual(RPackage):
	"""Automatic Differentiation with Dual Numbers

	Automatic differentiation is achieved by using dual numbers without
  providing hand-coded gradient functions. The output value of a mathematical 
  function is returned with the values of its exact first derivative 
  (or gradient). For more details see Baydin, Pearlmutter, Radul, and Siskind
  (2018) <https://jmlr.org/papers/volume18/17-468/17-468.pdf>.
	"""
	
	cran = "dual" 

	version("0.0.5", md5="c784e4ccb372d3d683db2f6cf44b24dd")

	depends_on("r@3.2:", type=("build", "run"))
