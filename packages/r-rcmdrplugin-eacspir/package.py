# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginEacspir(RPackage):
	"""Plugin de R-Commander para el Manual 'EACSPIR'

	Este paquete proporciona una interfaz grafica de usuario (GUI) para algunos de los procedimientos estadisticos detallados en un curso de 'Estadistica aplicada a las Ciencias Sociales mediante el programa informatico R' (EACSPIR). LA GUI se ha desarrollado como un Plugin del programa R-Commander.
	"""
	
	cran = "RcmdrPlugin.EACSPIR" 

	version("0.2-3", md5="48f5d1eff333488bca87ee82d141449d")

	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-ez", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rcmdr@2.8.0:", type=("build", "run"))
	depends_on("r-rcmdrmisc", type=("build", "run"))
