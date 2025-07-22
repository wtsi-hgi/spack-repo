# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeta7(RPackage):
	"""Rodriguez et al. (2004) Differential Gene Expression by Memory/Effector T Helper Cells Bearing the Gut-Homing Receptor Integrin alpha4 beta7.

	Data from 6 gpr files aims to identify differential expressed genes between the beta 7+ and beta 7- memory T helper cells.
	"""
	
	bioc = "beta7" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/beta7_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/beta7/beta7_1.40.0.tar.gz"]

	version("1.40.0", sha256="1b8cfbc530abe06a37f9db899c3e843748e68a2a24d6062a04d1732b77bde7e0", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/beta7_1.40.0.tar.gz")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))

