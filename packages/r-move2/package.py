# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMove2(RPackage):
	"""Processing and Analysing Animal Trajectories

	Tools to handle, manipulate and explore trajectory data, with an emphasis on data from tracked animals. The package is designed to support large studies with several million location records and keep track of units where possible. Data import directly from 'movebank' <https://www.movebank.org/cms/movebank-main> and files is facilitated.
	"""
	
	homepage = "https://bartk.gitlab.io/move2/"
	cran = "move2" 

	version("0.2.7", md5="a5931c9772f5781ae7ac65bc73ed689b", url="https://cran.r-project.org/src/contrib/move2_0.2.7.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-sf@1.0.12:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vroom@1.6.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-vctrs@0.5.2:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
