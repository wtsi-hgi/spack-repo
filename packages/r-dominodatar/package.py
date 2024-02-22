# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDominodatar(RPackage):
	"""'Domino Data R SDK'

	A wrapper on top of the 'Domino Data Python SDK' library. It lets 
    you query and access 'Domino Data Sources' directly from your R environment.
    Under the hood, 'Domino Data R SDK' leverages the API provided by the 
    'Domino Data Python SDK', which must be installed as a prerequisite.
    'Domino' is a platform that makes it easy to run your code on scalable 
    hardware, with integrated version control and collaboration features 
    designed for analytical workflows. See 
    <https://docs.dominodatalab.com/en/latest/api_guide/140b48/domino-data-api>
    for more information.
	"""
	
	homepage = "https://github.com/dominodatalab/DominoDataR"
	cran = "DominoDataR" 

	version("0.2.3", md5="b8d181cb6250a9f11516a1e35851607d")

	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-configparser", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
