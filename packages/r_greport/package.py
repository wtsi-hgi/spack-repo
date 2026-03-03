# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreport(RPackage):
	"""Graphical Reporting for Clinical Trials

	Contains many functions useful for
    monitoring and reporting the results of clinical trials and other
    experiments in which treatments are compared.  LaTeX is
    used to typeset the resulting reports, recommended to be in the
    context of 'knitr'. The 'Hmisc', 'ggplot2', and 'lattice' packages are used
    by 'greport' for high-level graphics.
	"""
	
	homepage = "http://hbiostat.org/R/greport/"
	cran = "greport" 

	version("0.7-4", md5="a4211db6bff787454fb1a0c903df42b6")

	depends_on("r-hmisc@4.0.0:", type=("build", "run"))
	depends_on("r-rms@5.0.0:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
