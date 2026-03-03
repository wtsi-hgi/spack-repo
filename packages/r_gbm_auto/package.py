# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbmAuto(RPackage):
	"""Automated Boosted Regression Tree Modelling and Mapping Suite

	Automates delta log-normal boosted regression tree abundance
    prediction. Loops through parameters provided (LR (learning rate), TC
    (tree complexity), BF (bag fraction)), chooses best, simplifies, &
    generates line, dot & bar plots, & outputs these & predictions & a
    report, makes predicted abundance maps, and Unrepresentativeness
    surfaces.  Package core built around 'gbm' (gradient boosting machine)
    functions in 'dismo' (Hijmans, Phillips, Leathwick & Jane Elith, 2020
    & ongoing), itself built around 'gbm' (Greenwell, Boehmke, Cunningham
    & Metcalfe, 2020 & ongoing, originally by Ridgeway). Indebted to
    Elith/Leathwick/Hastie 2008 'Working Guide'
    <doi:10.1111/j.1365-2656.2008.01390.x>; workflow follows Appendix S3.
    See <http://www.simondedman.com/> for published guides and papers
    using this package.
	"""
	
	cran = "gbm.auto" 

	version("2023.08.31", md5="855f5f7304c8e3d252491af04e80a4fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-beepr@1.2:", type=("build", "run"))
	depends_on("r-dismo@1.3.14:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-gbm@2.1.1:", type=("build", "run"))
	depends_on("r-ggmap@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-ggspatial@1.1.9:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate@1.9.2:", type=("build", "run"))
	depends_on("r-mapplots@1.5:", type=("build", "run"))
	depends_on("r-metrics@0.1.4:", type=("build", "run"))
	depends_on("r-readr@2.1.4:", type=("build", "run"))
	depends_on("r-sf@0.9.7:", type=("build", "run"))
	depends_on("r-stars@0.6.3:", type=("build", "run"))
	depends_on("r-starsextra@0.2.7:", type=("build", "run"))
	depends_on("r-stringi@1.6.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-viridis@0.6.4:", type=("build", "run"))
