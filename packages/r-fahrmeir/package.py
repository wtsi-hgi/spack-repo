# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFahrmeir(RPackage):
	"""Data from the Book "Multivariate Statistical Modelling Based on
Generalized Linear Models", First Edition, by Ludwig Fahrmeir
and Gerhard Tutz

	Data and functions for the book "Multivariate Statistical 
              Modelling Based on Generalized Linear Models", first edition, by 
              Ludwig Fahrmeir and Gerhard Tutz.  Useful when using the book.
	"""
	
	cran = "Fahrmeir" 

	version("2016.5.31", md5="93b6686d329f6acefc479ab7a4ee0873")

	depends_on("r@2.1:", type=("build", "run"))
