# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabrs(RPackage):
	"""Laboratorio di "Ricerca Sociale con R"

	Dati, scripts e funzioni per il libro "Ricerca sociale con R. Concetti e funzioni base per la ricerca sociale" (Datasets, scripts and functions to support the book "Ricerca sociale con R. Concetti e funzioni base per la ricerca sociale"). 
	"""
	
	homepage = "https://www.agnesevardanega.eu/"
	cran = "LabRS" 

	version("0.1.0", md5="61560169f730adb31acad2763d9994a8")

	depends_on("r-knitr", type=("build", "run"))
