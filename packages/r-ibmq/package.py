# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbmq(RPackage):
	"""integrated Bayesian Modeling of eQTL data

	integrated Bayesian Modeling of eQTL data
	"""
	
	homepage = "http://www.rglab.org"
	bioc = "iBMQ" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/iBMQ_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/iBMQ/iBMQ_1.42.0.tar.gz"]

	version("1.42.0", md5="9737c0aee38670491b2f29f73dcb743c")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-biobase@2.16:", type=("build", "run"))
	depends_on("r-ggplot2@0.9.2:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
	depends_on("openmp", type=("build", "link", "run"))
