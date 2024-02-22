# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPetfinder(RPackage):
	"""'Petfinder' API Wrapper

	
  Wrapper of the 'Petfinder API' <https://www.petfinder.com/developers/v2/docs/> that implements 
  methods for interacting with and extracting data from the 'Petfinder' database. The 'Petfinder 
  REST API' allows access to the 'Petfinder' database, one of the largest online databases of 
  adoptable animals and animal welfare organizations across North America.
	"""
	
	homepage = "https://github.com/aschleg/PetfindeR"
	cran = "PetfindeR" 

	version("2.1.0", md5="887d16c1b52645edf696c879a14f4e74")

	depends_on("r-r6", type=("build", "run"))
