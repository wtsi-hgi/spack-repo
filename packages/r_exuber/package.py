# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExuber(RPackage):
	"""Econometric Analysis of Explosive Time Series

	Testing for and dating periods of explosive
    dynamics (exuberance) in time series using the univariate and panel
    recursive unit root tests proposed by Phillips et al. (2015)
    <doi:10.1111/iere.12132> and Pavlidis et al. (2016)
    <doi:10.1007/s11146-015-9531-2>.The recursive least-squares
    algorithm utilizes the matrix inversion lemma to avoid matrix
    inversion which results in significant speed improvements. Simulation
    of a variety of periodically-collapsing bubble processes. Details can be 
    found in Vasilopoulos et al. (2022) <doi:10.18637/jss.v103.i10>.
	"""
	
	homepage = "https://github.com/kvasilopoulos/exuber"
	cran = "exuber" 

	version("1.0.2", md5="27d1ff5a706ec529a8e49479584d8c43")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cli@1.1:", type=("build", "run"))
	depends_on("r-dorng@1.8.2:", type=("build", "run"))
	depends_on("r-dosnow@1.0.16:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-generics@0.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rcpp@1.0.1:", type=("build", "run"))
	depends_on("r-rlang@0.3.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.2:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.400.2:", type=("build", "run"))
