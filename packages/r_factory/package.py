# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactory(RPackage):
	"""Build Function Factories

	Function factories are functions that make functions. They can be 
    confusing to construct. Straightforward techniques can produce functions 
    that are fragile or hard to understand. While more robust techniques exist 
    to construct function factories, those techniques can be confusing. This 
    package is designed to make it easier to construct function factories.
	"""
	
	homepage = "https://github.com/jonthegeek/factory"
	cran = "factory" 

	version("0.1.0", md5="95df96f27657142b476074c74aedb5b6")

	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
