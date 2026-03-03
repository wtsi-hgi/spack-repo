# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaber(RPackage):
	"""Split and Recombine Your Data

	Sometimes you need to split your data and work on the two chunks independently before bringing them back together. 'Taber' allows you to do that with its two functions.
	"""
	
	homepage = "https://github.com/restonslacker/taber"
	cran = "taber" 

	version("0.1.2", md5="020420bddca462c5d3fa93c4f8c0eecc")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
