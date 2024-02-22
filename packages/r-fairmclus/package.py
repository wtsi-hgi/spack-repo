# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFairmclus(RPackage):
	"""Clustering for Data with Sensitive Attribute

	Clustering for categorical and mixed-type of data, to preventing classification biases due to race, 
            gender or others sensitive attributes.
            This algorithm is an extension of the methodology proposed by "Santos & Heras (2020) <doi:10.28945/4643>".
	"""
	
	cran = "FairMclus" 

	version("2.2.1", md5="8692f3e28ff8486f1ab6ee564748c1d6")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
