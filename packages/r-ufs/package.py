# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUfs(RPackage):
	"""A Collection of Utilities

	This is a new version of the 'userfriendlyscience' package,
    which has grown a bit unwieldy. Therefore, distinct functionalities
    are being 'consciously uncoupled' into different packages. This package
    contains the general-purpose tools and utilities (see the
    'behaviorchange' package, the 'rosetta' package, and the
    soon-to-be-released 'scd' package for other functionality), and
    is the most direct 'successor' of the original 'userfriendlyscience' package.
    For example, this package contains a number of basic functions to create
    higher level plots, such as diamond plots, to easily plot sampling
    distributions, to generate confidence intervals, to plan study sample sizes
    for confidence intervals, and to do some basic operations such as
    (dis)attenuate effect size estimates.
	"""
	
	homepage = "https://ufs.opens.science"
	cran = "ufs" 

	version("0.5.10", md5="2420985614b5b63e7121d1f68cc90305")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-digest@0.6.19:", type=("build", "run"))
	depends_on("r-diptest@0.75.7:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.8:", type=("build", "run"))
	depends_on("r-ggridges@0.5:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-gtable@0.2:", type=("build", "run"))
	depends_on("r-htmltools@0.4:", type=("build", "run"))
	depends_on("r-kableextra@1.1:", type=("build", "run"))
	depends_on("r-knitr@1.22:", type=("build", "run"))
	depends_on("r-pander@0.6.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-rmdpartials@0.5.8:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-suppdists@1.1.9:", type=("build", "run"))
