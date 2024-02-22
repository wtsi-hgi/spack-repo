# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQicharts(RPackage):
	"""Quality Improvement Charts

	Functions for making run charts 
    [Anhoej, Olesen (2014) <doi:10.1371/journal.pone.0113825>] and basic
    Shewhart control charts [Mohammed, Worthington, Woodall (2008)
    <doi:10.1136/qshc.2004.012047>] for measure and count data.
    The main function, qic(), creates run and control charts and has a
    simple interface with a rich set of options to control data analysis
    and plotting, including options for automatic data aggregation by
    subgroups, easy analysis of before-and-after data, exclusion of one
    or more data points from analysis, and splitting charts into
    sequential time periods.
    Missing values and empty subgroups are handled gracefully.
	"""
	
	cran = "qicharts" 

	version("0.5.8", md5="3387a96fdd934e1ad0fb1db8e6e2fc11")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
