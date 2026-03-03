# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnicode(RPackage):
	"""Unicode Data and Utilities

	Data from Unicode 15.1.0 and related utilities.
	"""
	
	cran = "Unicode" 

	version("15.1.0-1", md5="3eaacee5bdd914142387d9ecabbfd8d9")

	depends_on("r@3.5:", type=("build", "run"))
