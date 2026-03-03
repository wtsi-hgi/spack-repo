# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDefault(RPackage):
	"""Change the Default Arguments in R Functions

	A simple syntax to change the default values for function
  arguments, whether they are in packages or defined locally.
	"""
	
	cran = "default" 

	version("1.0.0", md5="fec013bb7f84445aaca765c72d2c4d78")

