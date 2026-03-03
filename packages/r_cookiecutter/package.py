# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCookiecutter(RPackage):
	"""Generate Project Files from a Template

	Generate project files and directories following a pre-made template.
  You can specify variables to customize file names and content, and
  flexibly adapt the template to your needs. 'cookiecutter' for 'R'
  implements a subset of the excellent 'cookiecutter' package for the
  'Python' programming language (<https://github.com/cookiecutter/>), and
  aims to be largely compatible with the original 'cookiecutter' template
  format.
	"""
	
	homepage = "https://github.com/felixhenninger/cookiecutter/"
	cran = "cookiecutter" 

	version("0.1.0", md5="264875c0784b7336a6e7bcc04fefb8c5")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
