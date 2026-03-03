# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRosetta(RPackage):
	"""Parallel Use of Statistical Packages in Teaching

	When teaching statistics, it can often be desirable to
  uncouple the content from specific software packages. To ease such
  efforts, the Rosetta Stats website (<https://rosettastats.com>) allows
  comparing analyses in different packages. This package is the companion
  to the Rosetta Stats website, aiming to provide functions that produce
  output that is similar to output from other statistical packages, thereby
  facilitating 'software-agnostic' teaching of statistics.
	"""
	
	homepage = "https://r-packages.gitlab.io/rosetta/"
	cran = "rosetta" 

	version("0.3.12", md5="1d977d1968ffe06b2037d413cec76c5b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-car@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-ggrepel@0.8:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-lavaan@0.6.5:", type=("build", "run"))
	depends_on("r-lme4@1.1.19:", type=("build", "run"))
	depends_on("r-multcompview@0.1:", type=("build", "run"))
	depends_on("r-pander@0.6.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-psych@1.8.4:", type=("build", "run"))
	depends_on("r-pwr@1.2.2:", type=("build", "run"))
	depends_on("r-rmdpartials@0.5.8:", type=("build", "run"))
	depends_on("r-ufs@0.5.2:", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-sjstats", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
