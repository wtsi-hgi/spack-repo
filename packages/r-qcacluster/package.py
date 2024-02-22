# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcacluster(RPackage):
	"""Tools for the Analysis of Clustered Data in QCA

	Clustered set-relational data in Qualitative Comparative Analysis
    (QCA) can have a hierarchical structure, a panel structure or repeated cross
    sections. 'QCAcluster' allows QCA researchers to supplement the analysis
    of pooled the data with a disaggregated perspective focusing on selected 
    partitions of the data. The pooled data can be partitioned along the 
    dimensions of the clustered data (individual cross sections or time series) 
    to perform partition-specific truth table minimizations. Empirical 
    researchers can further calculate the weight that each partition has on the 
    parameters of the pooled solution and the diversity of the cases under 
    analysis within and across partitions 
    (see <https://ingorohlfing.github.io/QCAcluster/>).
	"""
	
	homepage = "https://github.com/ingorohlfing/QCAcluster"
	cran = "QCAcluster" 

	version("0.1.0", md5="2dfae88423d33461549e938cd79f4a65")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-plyr@1.8.5:", type=("build", "run"))
	depends_on("r-qca@3.7:", type=("build", "run"))
	depends_on("r-testit@0.11:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-upsetr@1.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringi@1.7.4:", type=("build", "run"))
	depends_on("r-rlist@0.4.6.1:", type=("build", "run"))
