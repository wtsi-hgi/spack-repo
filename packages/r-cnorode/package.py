# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnorode(RPackage):
	"""ODE add-on to CellNOptR

	Logic based ordinary differential equation (ODE) add-on to CellNOptR.
	"""
	
	bioc = "CNORode" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNORode_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNORode/CNORode_1.44.0.tar.gz"]

	version("1.44.0", sha256="876e053a8d3510a7be608c206c1ca2be789784539072aa25e4d05bb17785bd36")

	depends_on("r-cellnoptr", type=("build", "run"))
	depends_on("r-genalg", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
