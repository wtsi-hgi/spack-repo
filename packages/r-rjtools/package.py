# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjtools(RPackage):
	"""Preparing, Checking, and Submitting Articles to the 'R Journal'

	Create an 'R Journal' 'Rmarkdown' template article, that will
  generate html and pdf versions of your paper. Check that the paper folder 
  has all the required components needed for submission. 
  Examples of 'R Journal' publications can be found at 
  <https://journal.r-project.org>. 
	"""
	
	homepage = "https://github.com/rjournal/rjtools"
	cran = "rjtools" 

	version("1.0.12", md5="aa6d585302a0c31c4bdf0b3907aeb60f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-distill", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-hunspell", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-yesno", type=("build", "run"))
	depends_on("r-tinytex", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
