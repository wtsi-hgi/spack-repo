# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsminer(RPackage):
	"""Performance Spectrum Miner for Event Data

	Compute detailed and aggregated performance spectrum for event data. The detailed performance spectrum describes the event data in terms of segments, where the performance of each segment is measured and plotted for any occurrences of this segment over time and can be classified, e.g., regarding the overall population. The aggregated performance spectrum visualises the amount of cases of particular performance over time. Denisov, V., Fahland, D., & van der Aalst, W. M. P. (2018) <doi:10.1007/978-3-319-98648-7_9>.
	"""
	
	homepage = "https://bupar.net/"
	cran = "psmineR" 

	version("0.1.0", md5="4dd1bede98df7f794ff91140ffeaa28c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bupar@0.5.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
