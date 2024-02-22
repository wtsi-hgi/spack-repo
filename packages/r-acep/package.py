# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcep(RPackage):
	"""Analisis Computacional de Eventos de Protesta

	La libreria 'ACEP' contiene funciones especificas para
    desarrollar analisis computacional de eventos de protesta. Asimismo,
    contiene base de datos con colecciones de notas sobre protestas y
    diccionarios de palabras conflictivas. Coleccion de diccionarios que
    reune diccionarios de diferentes origenes.  The 'ACEP' library
    contains specific functions to perform computational analysis of
    protest events. It also contains a database with collections of notes
    on protests and dictionaries of conflicting words. Collection of
    dictionaries that brings together dictionaries from different sources.
	"""
	
	homepage = "https://github.com/agusnieto77/ACEP"
	cran = "ACEP" 

	version("0.0.22", md5="853dfc76be90b09028287d9f5809a6d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
