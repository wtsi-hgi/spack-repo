# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpiro(RPackage):
	"""Manage Data from Cardiopulmonary Exercise Testing

	Import, process, summarize and visualize raw data from 
    metabolic carts. See Robergs, Dwyer, and Astorino (2010) <doi:10.2165/11319670-000000000-00000> for more details on data processing. 
	"""
	
	homepage = "https://github.com/ropensci/spiro"
	cran = "spiro" 

	version("0.2.1", md5="76bcb96af73f979cfca11cc788d34717")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
