# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllmt(RPackage):
	"""Acute Lymphoblastic Leukemia Maintenance Therapy Analysis

	Evaluates acute lymphoblastic leukemia maintenance therapy practice at patient and cohort level.
	"""
	
	homepage = "https://github.com/tmungle/allMT"
	cran = "allMT" 

	version("0.1.0", md5="9eef24c729d14ae7c1e8699e792e89b7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-htmltable@2.2.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-rio@0.5.29:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-survival@3.2.11:", type=("build", "run"))
	depends_on("r-survminer@0.4.9:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
