# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSofi(RPackage):
	"""Interfaz interactiva con fines didacticos

	Este paquete tiene la finalidad de ayudar a aprender de una forma interactiva, teniendo ejemplos y la posibilidad de resolver nuevos al mismo tiempo. Apuntes de clase interactivos.
	"""
	
	homepage = "http://www.sofi.uno/"
	cran = "Sofi" 

	version("0.16.4.8", md5="7c7d7382f1e73c8927bc4bb504d8fa3d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
