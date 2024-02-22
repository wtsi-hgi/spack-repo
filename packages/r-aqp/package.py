# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAqp(RPackage):
	"""Algorithms for Quantitative Pedology

	The Algorithms for Quantitative Pedology (AQP) project was started in 2009 to organize a loosely-related set of concepts and source code on the topic of soil profile visualization, aggregation, and classification into this package (aqp). Over the past 8 years, the project has grown into a suite of related R packages that enhance and simplify the quantitative analysis of soil profile data. Central to the AQP project is a new vocabulary of specialized functions and data structures that can accommodate the inherent complexity of soil profile information; freeing the scientist to focus on ideas rather than boilerplate data processing tasks <doi:10.1016/j.cageo.2012.10.020>. These functions and data structures have been extensively tested and documented, applied to projects involving hundreds of thousands of soil profiles, and deeply integrated into widely used tools such as SoilWeb <https://casoilresource.lawr.ucdavis.edu/soilweb-apps/>. Components of the AQP project (aqp, soilDB, sharpshootR, soilReports packages) serve an important role in routine data analysis within the USDA-NRCS Soil Science Division. The AQP suite of R packages offer a convenient platform for bridging the gap between pedometric theory and practice.
	"""
	
	homepage = "https://github.com/ncss-tech/aqp"
	cran = "aqp" 

	version("2.0.2", md5="a028402977c22648aa0baebc4794f027")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
