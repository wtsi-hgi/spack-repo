# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResumer(RPackage):
	"""Build Resumes with R

	Using a CSV, LaTeX and R to easily build attractive resumes.
	"""
	
	homepage = "https://github.com/jaredlander/resumer"
	cran = "resumer" 

	version("0.0.5", md5="bf9d7541bfab6751c5372c634df59b68")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-useful", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
