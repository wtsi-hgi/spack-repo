# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcl(RPackage):
	"""Claims Reserving under the Double Chain Ladder Model

	Statistical modelling and forecasting in claims reserving in non-life insurance under the Double Chain Ladder framework by Martinez-Miranda, Nielsen and Verrall (2012).
	"""
	
	cran = "DCL" 

	version("0.1.2", md5="7f8d20071b7d611035717864a465a866")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
