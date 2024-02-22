# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDafishr(RPackage):
	"""Download, Wrangle, and Analyse Vessel Monitoring System Data

	Allows to download, clean and analyse raw Vessel Monitoring System, VMS, data from
    Mexican government. You can use the vms_download() function to
    download raw data, or you can use the sample_dataset provided within
    the package. You can follow the tutorial in the vignette available at
    <https://cbmc-gcmp.github.io/dafishr/index.html>.
	"""
	
	homepage = "https://github.com/CBMC-GCMP/dafishr"
	cran = "dafishr" 

	version("1.0.0", md5="0d74813479e659c871c1574dc8edcaf1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
