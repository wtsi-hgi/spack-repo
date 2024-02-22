# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutomagic(RPackage):
	"""Automagically Document and Install Packages Necessary to Run R
Code

	Parse R code in a given directory for R packages and attempt to install them from CRAN or GitHub. Optionally use a dependencies file for tighter control over which package versions to install.
	"""
	
	homepage = "https://github.com/cole-brokamp/automagic"
	cran = "automagic" 

	version("0.5.1", md5="dd8ba2e2fd22a70f1e841a3a5db51db9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
