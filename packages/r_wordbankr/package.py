# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordbankr(RPackage):
	"""Accessing the Wordbank Database

	Connecting to Wordbank, an open repository for developmental
    vocabulary data. For more information on the underlying data, see
    <http://wordbank.stanford.edu>.
	"""
	
	homepage = "https://langcog.github.io/wordbankr/"
	cran = "wordbankr" 

	version("1.0.3", md5="ab6a163a26ccddf652dc845a39b21924")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-dbi@1.1.3:", type=("build", "run"))
	depends_on("r-dbplyr@2.3.4:", type=("build", "run"))
	depends_on("r-dplyr@1.1.3:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.7:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-quantreggrowth@1.7.0:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-rmysql@0.10.26:", type=("build", "run"))
	depends_on("r-robustbase@0.99.0:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
