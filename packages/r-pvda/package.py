# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvda(RPackage):
	"""Disproportionality Functions for Pharmacovigilance

	Tools for performing disproportionality analysis using the information component, proportional reporting rate and the reporting odds ratio. The anticipated use is passing data to the da() function, which executes the disproportionality analysis. See Norén G.N., Hopstadius J. and Bate A. (2011) <doi:10.1177/0962280211403604> and Montastruc J.-L., Sommet A., Bagheri H. and Lapeyre-Mestre, M. (2011) <doi:10.1111/j.1365-2125.2011.04037.x> for further details.
	"""
	
	homepage = "https://oskargauffin.github.io/pvda/"
	cran = "pvda" 

	version("0.0.2", md5="0c8930876e58bc279f67b33ccd1a8795")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-cli@3.4.1:", type=("build", "run"))
	depends_on("r-data-table@1.14.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-dtplyr@1.2.2:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.5:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
