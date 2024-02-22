# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIggeneusage(RPackage):
	"""Differential gene usage in immune repertoires

	Detection of biases in the usage of immunoglobulin (Ig) genes is an important task in immune repertoire profiling. IgGeneUsage detects aberrant Ig gene usage between biological conditions using a probabilistic model which is analyzed computationally by Bayes inference. With this IgGeneUsage also avoids some common problems related to the current practice of null-hypothesis significance testing.
	"""
	
	homepage = "https://github.com/snaketron/IgGeneUsage"
	bioc = "IgGeneUsage" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/IgGeneUsage_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/IgGeneUsage/IgGeneUsage_1.16.0.tar.gz"]

	version("1.16.0", md5="231f1af3465f435ca3bb099a93e51e5b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
