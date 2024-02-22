# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRchallenge(RPackage):
	"""A Simple Data Science Challenge System

	A simple data science challenge system using R Markdown and 'Dropbox' <https://www.dropbox.com/>.
    It requires no network configuration, does not depend on external platforms
    like e.g. 'Kaggle' <https://www.kaggle.com/> and can be easily installed on a personal computer.
	"""
	
	homepage = "https://adrien.tspace.fr/rchallenge/"
	cran = "rchallenge" 

	version("1.3.4", md5="54dfad1883671c7fe157f48041d111b1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rmarkdown@0.5.1:", type=("build", "run"))
	depends_on("r-knitr@1.6:", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
