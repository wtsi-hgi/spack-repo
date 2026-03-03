# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcadapt(RPackage):
	"""Fast Principal Component Analysis for Outlier Detection

	Methods to detect genetic markers involved in biological
    adaptation. 'pcadapt' provides statistical tools for outlier detection based on
    Principal Component Analysis. Implements the method described in (Luu, 2016)
    <DOI:10.1111/1755-0998.12592> and later revised in (Privé, 2020) 
    <DOI:10.1093/molbev/msaa053>.
	"""
	
	homepage = "https://github.com/bcm-uga/pcadapt"
	cran = "pcadapt" 

	version("4.3.5", md5="6e479f6bc507085762c8b946cabfc98c")

	depends_on("r-bigutilsr@0.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mmapcharr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rmio", type=("build", "run"))
