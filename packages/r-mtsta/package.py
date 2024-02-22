# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtsta(RPackage):
	"""Accessing the Red List of Montane Tree Species of the Tropical
Andes

	Access the 'Red List of Montane Tree Species of the Tropical Andes' Tejedor Garavito et al.(2014, ISBN:978-1-905164-60-8). This package allows users to search for globally threatened tree species within the andean montane forests, including cloud forests and seasonal (wet) forests above 1500 m a.s.l.
	"""
	
	homepage = "https://github.com/PaulESantos/mtsta"
	cran = "mtsta" 

	version("0.0.0.1", md5="f958d92f791fd12c18eb304ad95357b5")

	depends_on("r@2.10:", type=("build", "run"))
