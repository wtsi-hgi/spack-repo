# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdsarm(RPackage):
	"""Gauss - Dantzig Selector: Aggregation over Random Models

	The method aims to identify important factors in screening experiments by aggregation over random models as studied in Singh and Stufken (2022) <doi:10.48550/arXiv.2205.13497>. This package provides functions to run the Gauss-Dantzig selector on screening experiments when interactions may be affecting the response. Currently, all functions require each factor to be at two levels coded as +1 and -1. 
	"""
	
	homepage = "https://github.com/agrakhi/GDSARM"
	cran = "GDSARM" 

	version("0.1.1", md5="d9bc2a6b652cf8e58b8153f7a70b87a3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
