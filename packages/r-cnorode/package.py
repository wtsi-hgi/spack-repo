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

	version("1.44.0", md5="e93b3e3437c26f6cfab6690f78c6a6cc")

	depends_on("r-cellnoptr", type=("build", "run"))
	depends_on("r-genalg", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
