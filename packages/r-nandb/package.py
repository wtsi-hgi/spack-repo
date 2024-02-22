# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNandb(RPackage):
	"""Number and Brightness Image Analysis

	Calculation of molecular number and brightness from
    fluorescence microscopy image series. The software was published in a
    2016 paper <doi:10.1093/bioinformatics/btx434>. The seminal paper for
    the technique is Digman et al. 2008 <doi:10.1529/biophysj.107.114645>.
    A review of the technique was published in 2017
    <doi:10.1016/j.ymeth.2017.12.001>.
	"""
	
	homepage = "https://rorynolan.github.io/nandb/"
	cran = "nandb" 

	version("2.1.0", md5="a1990ee27256c0383e816a79dd7cca9d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-autothresholdr@1.3.11:", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-checkmate@1.9.3:", type=("build", "run"))
	depends_on("r-detrendr@0.6.12:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-filesstrings@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-ijtiff@2.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp@1.0.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang@0.3.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-withr@2.1:", type=("build", "run"))
