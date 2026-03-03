# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModulecolor(RPackage):
	"""Basic Module Functions

	Methods for color labeling, calculation of eigengenes, merging of closely related modules.
	"""
	
	homepage = "https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/BranchCutting/"
	cran = "moduleColor" 

	version("1.8-4", md5="2bd2751a9421c928aacef73a85088886")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
