# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListwithdefaults(RPackage):
	"""List with Defaults

	Provides a function that, as an alternative to base::list, allows
    default values to be inherited from another list.
	"""
	
	homepage = "https://github.com/drknexus/listWithDefaults"
	cran = "listWithDefaults" 

	version("1.2.0", md5="727833230a4bd27958b67c852fdd2157")

	depends_on("r-assertthat", type=("build", "run"))
