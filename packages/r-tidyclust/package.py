# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyclust(RPackage):
	"""A Common API to Clustering

	A common interface to specifying clustering models, in the
    same style as 'parsnip'. Creates unified interface across different
    functions and computational engines.
	"""
	
	homepage = "https://github.com/tidymodels/tidyclust"
	cran = "tidyclust" 

	version("0.2.1", md5="5ca1619811e08c46318e6b48d72dd911")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-dials@1.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-flexclust@1.3.6:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-hardhat@1:", type=("build", "run"))
	depends_on("r-modelenv@0.1:", type=("build", "run"))
	depends_on("r-parsnip@1.0.2:", type=("build", "run"))
	depends_on("r-prettyunits@1.1:", type=("build", "run"))
	depends_on("r-rfast@2.0.6:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-rsample@1:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-tune@1:", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
