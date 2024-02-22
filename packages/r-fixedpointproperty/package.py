# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFixedpointproperty(RPackage):
	"""Determine and Test the Fixed-Point Property in Binary Mixture
Data

	Determine and test the fixed-point property in binary mixture data.
  This package was originally developed in the context of detecting mixture of 
  cognitive processing strategies, based on observed response time distributions. 
  The method is explain in more detail by Van Maanen, De Jong, Van Rijn (2014) 
  <doi:10.1371/journal.pone.0106113> and Van Maanen, Couto, Lebreton, (2016) 
  <doi:10.1371/journal.pone.0167377>.
	"""
	
	cran = "fixedpointproperty" 

	version("1.0", md5="2c40033d01c9fbcd1f20da21a29e0988")

	depends_on("r-bayesfactor", type=("build", "run"))
