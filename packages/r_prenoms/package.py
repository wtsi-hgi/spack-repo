# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrenoms(RPackage):
	"""Names Given to Babies in Quebec Between 1980 and 2020

	A database containing the names 
  of the babies born in Quebec between 1980 and 2020.
	"""
	
	homepage = "<https://github.com/desautm/prenoms>"
	cran = "prenoms" 

	version("0.0.1", md5="6040b35bc4639b12f741d5af55791b9f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
