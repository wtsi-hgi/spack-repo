# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmtools(RPackage):
	"""Tools for Clinical Data Management

	For checking the dataset from EDC(Electronic Data Capture) in clinical trials.
             'dmtools' reshape your dataset in a tidy view and check events.
             You can reshape the dataset and choose your target to check, for example, the laboratory reference range.
	"""
	
	homepage = "https://github.com/KonstantinRyabov/dmtools"
	cran = "dmtools" 

	version("0.2.6", md5="ed09922974487ca8e04bbd9b66cdbe9e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
