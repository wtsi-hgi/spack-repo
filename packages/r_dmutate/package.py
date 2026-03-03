# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmutate(RPackage):
	"""Mutate Data Frames with Random Variates

	Work within the 'dplyr' workflow to add random variates to your data frame. 
  Variates can be added at any level of an existing column.  Also, bounds can be specified 
  for simulated variates. 
	"""
	
	homepage = "https://github.com/kylebaron/dmutate"
	cran = "dmutate" 

	version("0.1.3", md5="fe3847b1c8a0f021e3346fe1ccd24051")

	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
