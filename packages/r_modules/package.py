# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModules(RPackage):
	"""Self Contained Units of Source Code

	Provides modules as an organizational unit for source code. Modules
    enforce to be more rigorous when defining dependencies and have
    a local search path. They can be used as a sub unit within packages
    or in scripts.
	"""
	
	homepage = "https://github.com/wahani/modules"
	cran = "modules" 

	version("0.13.0", md5="3a07ad7260c200f44081628ead32ffbf")

	depends_on("r@3.2:", type=("build", "run"))
