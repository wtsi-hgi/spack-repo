# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroupdata2(RPackage):
	"""Creating Groups from Data

	Methods for dividing data into groups. 
    Create balanced partitions and cross-validation folds. 
    Perform time series windowing and general grouping and splitting of data. 
    Balance existing groups with up- and downsampling or collapse them to fewer groups.
	"""
	
	homepage = "https://github.com/ludvigolsen/groupdata2"
	cran = "groupdata2" 

	version("2.0.3", md5="44b3b6e751d8a3f3ea6d3b8bb434a5a2", url="https://cran.r-project.org/src/contrib/groupdata2_2.0.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-numbers@0.7.5:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-plyr@1.8.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rearrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
