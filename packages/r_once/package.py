# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnce(RPackage):
	"""Execute Expensive Operations Only Once

	Allows you to easily execute expensive compute operations only once, and save the resulting object to disk.
	"""
	
	homepage = "https://gdmcdonald.github.io/once/"
	cran = "once" 

	version("0.4.1", md5="485a17db8a705719335e68b537e5dcf8")

	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
