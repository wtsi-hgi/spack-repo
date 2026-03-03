# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCherryblossom(RPackage):
	"""Cherry Blossom Run Race Results

	Race results of the Cherry Blossom Run, which is an annual road race that takes place in Washington, DC.
	"""
	
	homepage = "https://github.com/OpenIntroStat/cherryblossom"
	cran = "cherryblossom" 

	version("0.1.0", md5="81fb2dbca6a0abbaee3319bc6efb59ce")

	depends_on("r@2.10:", type=("build", "run"))
