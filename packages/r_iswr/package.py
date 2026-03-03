# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIswr(RPackage):
	"""Introductory Statistics with R

	Data sets and scripts for text examples and exercises in 
  P. Dalgaard (2008), `Introductory Statistics with R', 2nd ed., Springer Verlag, ISBN 978-0387790534.  
	"""
	
	cran = "ISwR" 

	version("2.0-8", md5="6adcd492d8948aaf4cf4a3b1a1fc792a")

	depends_on("r@2.6:", type=("build", "run"))
