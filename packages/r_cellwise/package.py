# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellwise(RPackage):
	"""Analyzing Data with Cellwise Outliers

	Tools for detecting cellwise outliers and robust methods to analyze
    data which may contain them. Contains the implementation of the algorithms described in
    Rousseeuw and Van den Bossche (2018) <doi:10.1080/00401706.2017.1340909> (open access)
    Hubert et al. (2019) <doi:10.1080/00401706.2018.1562989> (open access),
    Raymaekers and Rousseeuw (2021) <doi:10.1080/00401706.2019.1677270> (open access),
    Raymaekers and Rousseeuw (2021) <doi:10.1007/s10994-021-05960-5> (open access),
    Raymaekers and Rousseeuw (2021) <doi:10.52933/jdssv.v1i3.18> (open access),
    Raymaekers and Rousseeuw (2022) <arXiv:2207.13493> (open access)
    Rousseeuw (2022) <doi:10.1016/j.ecosta.2023.01.007> (open access).
    Examples can be found in the vignettes:
    "DDC_examples", "MacroPCA_examples", "wrap_examples", "transfo_examples",
    "DI_examples", "cellMCD_examples" , "Correspondence_analysis_examples",
    and "cellwise_weights_examples".
	"""
	
	cran = "cellWise" 

	version("2.5.3", md5="d11c65e7ad143d73ee1aae37426569e7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
