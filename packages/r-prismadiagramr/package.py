# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrismadiagramr(RPackage):
	"""Creates a Prisma Diagram using 'DiagrammeR'

	Creates 'PRISMA' <http://prisma-statement.org/> diagram from a minimal dataset of included and excluded studies and allows for more custom diagrams. 'PRISMA' diagrams are used to track the identification, screening, eligibility, and inclusion of studies in a systematic review. 
	"""
	
	homepage = "https://github.com/ltrainstg/prismadiagramR"
	cran = "prismadiagramR" 

	version("1.0.0", md5="7feeb61b833ccead25f88da5f74905e2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
