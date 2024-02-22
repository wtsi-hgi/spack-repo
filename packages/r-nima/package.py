# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNima(RPackage):
	"""Nima Hejazi's R Toolbox

	Miscellaneous R functions developed as collateral damage over the
    course of work in statistical and scientific computing for research. These
    include, for example, utilities that supplement existing idiosyncrasies of
    the R language, extend existing plotting functionality and aesthetics, help
    prepare data objects for imputation, and extend access to command line tools
    and systems-level information.
	"""
	
	homepage = "https://github.com/nhejazi/nima"
	cran = "nima" 

	version("0.6.2", md5="0b1e99ca31bd883c075a61d30f02d50a")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
