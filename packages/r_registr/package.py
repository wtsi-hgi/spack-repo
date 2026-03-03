# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegistr(RPackage):
	"""Curve Registration for Exponential Family Functional Data

	A method for performing joint registration and functional principal
    component analysis for curves (functional data) that are generated from exponential family distributions. This 
    mainly implements the algorithms described in 'Wrobel et al. (2019)' <doi:10.1111/biom.12963> and further adapts them to potentially
    incomplete curves where (some) curves are not observed from the beginning and/or until the end of the common domain. Curve registration 
    can be used to better understand patterns in functional data by separating curves into phase and amplitude variability.
    This software handles both binary and continuous functional data, and is
    especially applicable in accelerometry and wearable technology.
	"""
	
	cran = "registr" 

	version("2.1.0", md5="d53a35b0ff0e5d54eeb54213d9cb1ee0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pbs", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("icu4c", type=("build", "link", "run"))
	depends_on("libiconv", type=("build", "link", "run"))
