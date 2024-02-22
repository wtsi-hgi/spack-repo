# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArnie(RPackage):
	""""Arnie" box office records 1982-2014

	Arnold Schwarzenegger movie weekend box office records from
    1982-2014
	"""
	
	homepage = "https://github.com/imanuelcostigan/arnie"
	cran = "arnie" 

	version("0.1.2", md5="5a94a0e1e58f78f8ddbac49b25ec6c46")

	depends_on("r@3.1:", type=("build", "run"))
