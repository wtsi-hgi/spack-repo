# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMousetrap(RPackage):
	"""Process and Analyze Mouse-Tracking Data

	Mouse-tracking, the analysis of mouse movements in computerized
    experiments, is a method that is becoming increasingly popular in the
    cognitive sciences. The mousetrap package offers functions for importing,
    preprocessing, analyzing, aggregating, and visualizing mouse-tracking data.
    An introduction into mouse-tracking analyses using mousetrap can be found
    in Wulff, Kieslich, Henninger, Haslbeck, & Schulte-Mecklenbeck (2023)
    <doi:10.31234/osf.io/v685r> (preprint: 
    <https://osf.io/preprints/psyarxiv/v685r>).
	"""
	
	homepage = "https://pascalkieslich.github.io/mousetrap/"
	cran = "mousetrap" 

	version("3.2.3", md5="7de41b5d96f7428627da9ddabf53c040")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-psych@1.2.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-cstab", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
