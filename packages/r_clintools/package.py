# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClintools(RPackage):
	"""Tools for Clinical Research

	
   Every research team have their own script for data management, statistics and 
   most importantly hemodynamic indices. The purpose is to standardize scripts 
   utilized in clinical research. The hemodynamic indices can be used in a long-format dataframe, 
   and add both periods of interest (trigger-periods), and delete artifacts with deleter-files. 
   Transfer function analysis (Claassen et al. (2016) <doi:10.1177/0271678X15626425>) and
   Mx (Czosnyka et al. (1996) <doi:10.1161/01.str.27.10.1829>) can be calculated using this package.
	"""
	
	homepage = "https://github.com/lilleoel/clintools"
	cran = "clintools" 

	version("0.9.10.1", md5="3079c0a9f7ef5fd033432f121a97b63e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-signal@0.7.6:", type=("build", "run"))
	depends_on("r-xml2@1.3.2:", type=("build", "run"))
	depends_on("r-lme4@1.1.27.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-proc@1.18:", type=("build", "run"))
	depends_on("r-irr@0.84.1:", type=("build", "run"))
	depends_on("r-nlme@3.1.160:", type=("build", "run"))
	depends_on("r-parameters@0.19:", type=("build", "run"))
	depends_on("r-stringi@1.7.8:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-survival@3.4.0:", type=("build", "run"))
	depends_on("r-pander@0.6.5:", type=("build", "run"))
