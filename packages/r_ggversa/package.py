# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgversa(RPackage):
	"""Graficas Versatiles Con 'ggplot2'

	A collection of datasets for the upcoming book "Graficas versatiles con ggplot: Analisis visuales de datos", by Raymond L. Tremblay and Julian Hernandez-Serano. 
	"""
	
	cran = "ggversa" 

	version("0.0.1", md5="e6207ea02937f4fb50f83caf4490702f")

