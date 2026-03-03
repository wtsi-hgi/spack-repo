# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoiclaclu(RPackage):
	"""Classification and Clustering of Sequencing Data Based on a
Poisson Model

	Implements the methods described in the paper, Witten (2011) Classification and Clustering of Sequencing Data using a Poisson Model, Annals of Applied Statistics 5(4) 2493-2518.
	"""
	
	cran = "PoiClaClu" 

	version("1.0.2.1", md5="0b6a96b5e02ab7fcad913e7f6c538d12")

