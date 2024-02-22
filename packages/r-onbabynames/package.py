# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnbabynames(RPackage):
	"""Names Given to Babies in Ontario Between 1917 and 2018

	A database containing the names 
  of the babies born in Ontario between 1917 and 2018. 
  Counts of fewer than 5 names were suppressed for privacy.
	"""
	
	homepage = "<https://github.com/desautm/onbabynames>"
	cran = "onbabynames" 

	version("0.0.1", md5="105796e41e8970154fa4d62fd0517492")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
