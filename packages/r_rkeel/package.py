# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkeel(RPackage):
	"""Using 'KEEL' in R Code

	'KEEL' is a popular 'Java' software for a large number of different knowledge data discovery tasks.
    This package takes the advantages of 'KEEL' and R, allowing to use 'KEEL' algorithms in simple R code.
    The implemented R code layer between R and 'KEEL' makes easy both using 'KEEL' algorithms in R as implementing new algorithms for 'RKEEL' in a very simple way.
    It includes more than 100 algorithms for classification, regression, preprocess, association rules and imbalance learning, which allows a more complete experimentation process.
    For more information about 'KEEL', see <http://www.keel.es/>.
	"""
	
	cran = "RKEEL" 

	version("1.3.4", md5="b972e0119a939fbc0e1233be5a9c6ea2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-rkeeldata@1.0.5:", type=("build", "run"))
	depends_on("r-pmml", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
