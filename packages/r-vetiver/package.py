# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVetiver(RPackage):
	"""Version, Share, Deploy, and Monitor Models

	The goal of 'vetiver' is to provide fluent tooling to
    version, share, deploy, and monitor a trained model. Functions handle
    both recording and checking the model's input data prototype, and
    predicting from a remote API endpoint. The 'vetiver' package is
    extensible, with generics that can support many kinds of models.
	"""
	
	homepage = "https://vetiver.rstudio.com"
	cran = "vetiver" 

	version("0.2.5", md5="16d8cc9db67a04d255f70e2e5f23aa1a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bundle", type=("build", "run"))
	depends_on("r-butcher@0.3.1:", type=("build", "run"))
	depends_on("r-cereal", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-pins@1.3:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rapidoc", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
