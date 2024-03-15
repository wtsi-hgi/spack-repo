# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTheft(RPackage):
	"""Tools for Handling Extraction of Features from Time Series

	Consolidates and calculates different sets of time-series features from multiple
    'R' and 'Python' packages including 'Rcatch22' Henderson, T. (2021) <doi:10.5281/zenodo.5546815>,
    'feasts' O'Hara-Wild, M., Hyndman, R., and Wang, E. (2021) <https://CRAN.R-project.org/package=feasts>,
    'tsfeatures' Hyndman, R., Kang, Y., Montero-Manso, P., Talagala, T., Wang, E., Yang, Y., and O'Hara-Wild, M. (2020)
    <https://CRAN.R-project.org/package=tsfeatures>, 'tsfresh' Christ, M., Braun, N., Neuffer, J.,
    and Kempa-Liehr A.W. (2018) <doi:10.1016/j.neucom.2018.03.067>, 'TSFEL' Barandas, M., et al. (2020)
    <doi:10.1016/j.softx.2020.100456>, and 'Kats' Facebook Infrastructure Data Science (2021)
    <https://facebookresearch.github.io/Kats/>.
	"""
	
	homepage = "https://hendersontrent.github.io/theft/"
	cran = "theft" 

	version("0.6.1", md5="237081f34e4699221151e52cccef5368")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-fabletools", type=("build", "run"))
	depends_on("r-tsfeatures", type=("build", "run"))
	depends_on("r-feasts", type=("build", "run"))
	depends_on("r-rcatch22", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
