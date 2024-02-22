# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuaguas(RPackage):
	"""Nombres Inscritos en Chile (1920 - 2021)

	Datos de nombres inscritos en Chile
    entre 1920 y 2021, de acuerdo al Servicio de Registro Civil.
    English: Chilean baby names registered from 1920 to 2021
    by the Civil Registry Service.
	"""
	
	homepage = "https://github.com/rivaquiroga/guaguas"
	cran = "guaguas" 

	version("0.3.0", md5="84156a6e2550ac39f9d93686c6b82d15")

	depends_on("r@2.10:", type=("build", "run"))
