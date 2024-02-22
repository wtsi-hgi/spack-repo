# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbiascorrection(RPackage):
	"""Correct Bias in DNA Methylation Analyses

	Implementation of the algorithms (with minor modifications)
    to correct bias in quantitative DNA methylation analyses as described
    by Moskalev et al. (2011) <doi:10.1093/nar/gkr213>. Publication:
    Kapsner et al. (2021) <doi:10.1002/ijc.33681>.
	"""
	
	homepage = "https://github.com/kapsner/rBiasCorrection"
	cran = "rBiasCorrection" 

	version("0.3.4", md5="4ad5c6a859af1efd5fe87f06b31323ba")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
