# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForensit(RPackage):
	"""Information Theory Tools for Forensic Analysis

	The 'forensIT' package is a comprehensive statistical toolkit tailored for handling missing person cases. By leveraging information theory metrics, it enables accurate assessment of kinship, particularly when limited genetic evidence is available. With a focus on optimizing statistical power, 'forensIT' empowers investigators to effectively prioritize family members, enhancing the reliability and efficiency of missing person investigations.
	"""
	
	cran = "forensIT" 

	version("1.0.0", md5="0ddb8157ec0501455d94f71f0d66bf63")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mispitools", type=("build", "run"))
	depends_on("r-forrel", type=("build", "run"))
	depends_on("r-pedprobr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-fbnet", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-hrbrthemes", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-pedtools", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-paramlink", type=("build", "run"))
