# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfoaas(RPackage):
	"""R Interface to 'FOAAS'

	R access to the 'FOAAS' (F... Off As A Service) web service is provided.
	"""
	
	homepage = "https://github.com/eddelbuettel/rfoaas/"
	cran = "rfoaas" 

	version("2.3.2", md5="826db9597b06e7598708e8db74288d6f")

	depends_on("r-httr", type=("build", "run"))
