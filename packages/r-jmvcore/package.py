# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmvcore(RPackage):
	"""Dependencies for the 'jamovi' Framework

	A framework for creating rich interactive analyses for the jamovi
    platform (see <https://www.jamovi.org> for more information).
	"""
	
	homepage = "https://www.jamovi.org"
	cran = "jmvcore" 

	version("2.4.7", md5="f27afb95f291240751e3f530c16b6e28")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r6@1.0.1:", type=("build", "run"))
	depends_on("r-rlang@0.3.0.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
