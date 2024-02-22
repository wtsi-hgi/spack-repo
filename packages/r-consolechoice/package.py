# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsolechoice(RPackage):
	"""An Easy and Quick Way to Loop a Character Vector as a Menu in
the Console

	A fast way to loop a character vector or file names as a menu in the console for the
  user to choose an option.
	"""
	
	cran = "consolechoice" 

	version("1.1.1", md5="542e44087f7cdd6bcc8893c9f16c2b14")

