# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytominer(RPackage):
	"""Methods for Image-Based Cell Profiling

	Typical morphological profiling datasets have millions of cells
    and hundreds of features per cell. When working with this data, you must
    clean the data, normalize the features to make them comparable across
    experiments, transform the features, select features based on their
    quality, and aggregate the single-cell data, if needed. 'cytominer' makes
    these steps fast and easy. Methods used in practice in the field are
    discussed in Caicedo (2017) <doi:10.1038/nmeth.4397>. An overview of the
    field is presented in Caicedo (2016) <doi:10.1016/j.copbio.2016.04.003>.
	"""
	
	homepage = "https://github.com/cytomining/cytominer"
	cran = "cytominer" 

	version("0.2.2", md5="c21b7f683d786eee003a47840f97e08b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-caret@6.0.76:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-futile-logger@1.4.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
