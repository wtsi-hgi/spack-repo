# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgmql(RPackage):
	"""GenoMetric Query Language for R/Bioconductor

	This package brings the GenoMetric Query Language (GMQL) functionalities into the R environment. GMQL is a high-level, declarative language to manage heterogeneous genomic datasets for biomedical purposes, using simple queries to process genomic regions and their metadata and properties. GMQL adopts algorithms efficiently designed for big data using cloud-computing technologies (like Apache Hadoop and Spark) allowing GMQL to run on modern infrastructures, in order to achieve scalability and high performance. It allows to create, manipulate and extract genomic data from different data sources both locally and remotely. Our RGMQL functions allow complex queries and processing leveraging on the R idiomatic paradigm. The RGMQL package also provides a rich set of ancillary classes that allow sophisticated input/output management and sorting, such as: ASC, DESC, BAG, MIN, MAX, SUM, AVG, MEDIAN, STD, Q1, Q2, Q3 (and many others). Note that many RGMQL functions are not directly executed in R environment, but are deferred until real execution is issued.
	"""
	
	homepage = "http://www.bioinformatics.deib.polimi.it/genomic_computing/GMQL/"
	bioc = "RGMQL" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RGMQL_1.22.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RGMQL/RGMQL_1.22.1.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.1", sha256="4704a42a4f68b8e2d54433c7f739b0be0637362ee62afe173a02f1901e27d3fa")
	version("1.22.0", md5="78de1ecefadf0a7729bf7b62b50a2c1b")

	depends_on("r@3.4.2:", type=("build", "run"))
	depends_on("r-rgmqllib", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
