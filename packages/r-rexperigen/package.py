# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRexperigen(RPackage):
	"""R Interface to Experigen

	Provides convenience functions to communicate with
    an Experigen server: Experigen (<http://github.com/aquincum/experigen>)
    is an online framework for creating  linguistic experiments,
    and it stores the results on a dedicated server. This package can be
    used to retrieve the results from the server, and it is especially
    helpful with registered experiments, as authentication with the server
    has to happen.
	"""
	
	homepage = "https://github.com/aquincum/Rexperigen"
	cran = "Rexperigen" 

	version("0.2.1", md5="759541bd93ebaeff6e62446ffcbbfe5d")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
