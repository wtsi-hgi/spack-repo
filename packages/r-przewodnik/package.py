# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrzewodnik(RPackage):
	"""Datasets and Functions Used in the Book 'Przewodnik po Pakiecie
R'

	Data sets and functions used in the polish book 
    "Przewodnik po pakiecie R" (The Hitchhiker's Guide to the R). 
    See more at <http://biecek.pl/R>. Among others you will find here 
    data about housing prices, cancer patients, running times and many others.
	"""
	
	cran = "Przewodnik" 

	version("0.16.12", md5="875155918ad7025175915bd4d7491b43")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pogromcydanych", type=("build", "run"))
	depends_on("r-pbimisc", type=("build", "run"))
