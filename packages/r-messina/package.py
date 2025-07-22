# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMessina(RPackage):
	"""Single-gene classifiers and outlier-resistant detection of differential expression for two-group and survival problems

	Messina is a collection of algorithms for constructing optimally robust single-gene classifiers, and for identifying differential expression in the presence of outliers or unknown sample subgroups.  The methods have application in identifying lead features to develop into clinical tests (both diagnostic and prognostic), and in identifying differential expression when a fraction of samples show unusual patterns of expression.
	"""
	
	bioc = "messina" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/messina_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/messina/messina_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="4e3826cb5c1575afb615a5fd6de8a69278be092673d47369513f261d7b968525")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival@2.37.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr@1.8:", type=("build", "run"))
	depends_on("r-ggplot2@0.9.3.1:", type=("build", "run"))
	depends_on("r-foreach@1.4.1:", type=("build", "run"))
