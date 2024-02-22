# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginKmggplot2(RPackage):
	"""R Commander Plug-in for Data Visualization with 'ggplot2'

	A GUI front-end for 'ggplot2' supports Kaplan-Meier plot, histogram,
    Q-Q plot, box plot, errorbar plot, scatter plot, line chart, pie chart,
    bar chart, contour plot, and distribution plot.
	"""
	
	cran = "RcmdrPlugin.KMggplot2" 

	version("0.2-6", md5="b1bc789d2f656fee9dbabdedc5a6361c", url="https://cran.r-project.org/src/contrib/RcmdrPlugin.KMggplot2_0.2-6.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcmdr@2.6.0:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-ggthemes@4.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-survival@2.44.1.1:", type=("build", "run"))
	depends_on("r-tcltk2@1.2.11:", type=("build", "run"))
