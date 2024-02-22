# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThreewords(RPackage):
	"""Represent Precise Coordinates in Three Words

	A connector to the 'What3Words' (http://what3words.com/) service, which represents each 3m by 3m square on earth
             with a unique trio of English-language words.
	"""
	
	cran = "threewords" 

	version("0.1.0", md5="d9ebc785ab0c09080b1bf18d4830eff6")

	depends_on("r-httr", type=("build", "run"))
