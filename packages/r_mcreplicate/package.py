# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcreplicate(RPackage):
	"""Multi-Core Replicate

	Multi-core replication function to make it easier to do fast 
  Monte Carlo simulation. Based on the mcreplicate() function from the 
  'rethinking' package. The 'rethinking' package requires installing 'rstan', 
  which is onerous to install, while also not adding capabilities to this 
  function.
	"""
	
	cran = "mcreplicate" 

	version("0.1.2", md5="f7e184f8e82e4e5f73678d9de32f4781")

