# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDematel(RPackage):
	"""Decision Making Trial and Evaluation Laboratory Technique in R

	Developed to Solve the Multi-Criteria Decision Making Problems with Decision Making Trial and Evaluation Laboratory Technique in R.
	"""
	
	cran = "dematel" 

	version("0.1.0", md5="b834fb0499a17836cc0678dba59a0d69")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
