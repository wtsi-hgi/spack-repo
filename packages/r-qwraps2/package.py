# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQwraps2(RPackage):
	"""Quick Wraps 2

	A collection of (wrapper) functions the creator found useful
    for quickly placing data summaries and formatted regression results into
    '.Rnw' or '.Rmd' files. Functions for generating commonly used graphics,
    such as receiver operating curves or Bland-Altman plots, are also provided
    by 'qwraps2'.  'qwraps2' is a updated version of a package 'qwraps'. The
    original version 'qwraps' was never submitted to CRAN but can be found at
    <https://github.com/dewittpe/qwraps/>. The implementation and limited scope
    of the functions within 'qwraps2' <https://github.com/dewittpe/qwraps2/> is
    fundamentally different from 'qwraps'.
	"""
	
	homepage = "https://github.com/dewittpe/qwraps2/"
	cran = "qwraps2" 

	version("0.6.0", md5="9afead65ba448445f718a272cb64191a", url="https://cran.r-project.org/src/contrib/qwraps2_0.6.0.tar.gz")
	version("0.5.2", md5="0d178d92946eeef2bb2a270fec0a99c8", url="https://cran.r-project.org/src/contrib/Archive/qwraps2/qwraps2_0.5.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rcpp@0.12.11:", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
