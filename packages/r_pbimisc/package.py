# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbimisc(RPackage):
	"""A Set of Datasets Used in My Classes or in the Book 'Modele
Liniowe i Mieszane w R, Wraz z Przykladami w Analizie Danych'

	A set of datasets and functions used in the book
  'Modele liniowe i mieszane w R, wraz z przykladami w analizie danych'.
  Datasets either come from real studies or are created to be as similar 
  as possible to real studies.
	"""
	
	homepage = "http://www.biecek.pl/R/"
	cran = "PBImisc" 

	version("1.0", md5="6c159ae6a2cb3f7200df4882fcd0c232")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
