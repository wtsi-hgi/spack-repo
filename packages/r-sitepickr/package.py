# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSitepickr(RPackage):
	"""Two-Level Sample Selection with Optimal Site Replacement

	Carries out a two-level sample selection where the possibility of an initially selected site not wanting to participate is anticipated, and the site is optimally replaced. The procedure aims to reduce bias (and/or loss of external validity) with respect to the target population. In selecting units and sub-units, 'sitepickR' uses the cube method developed by 'Deville & Tillé', (2004) <http://www.math.helsinki.fi/msm/banocoss/Deville_Tille_2004.pdf> and described in Tillé (2011) <https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2011002/article/11609-eng.pdf?st=5-sx8Q8n>. The cube method is a probability sampling method that is designed to satisfy criteria for balance between the sample and the population. Recent research has shown that this method performs well in simulations for studies of educational programs (see Fay & Olsen (2021, under review). To implement the cube method, 'sitepickR' uses the sampling R package <https://cran.r-project.org/package=sampling>. To implement statistical matching, 'sitepickR' uses the 'MatchIt' R package <https://cran.r-project.org/package=MatchIt>.
	"""
	
	cran = "sitepickR" 

	version("0.0.1", md5="77e2af8a78ba652161c17014daa24d22")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
