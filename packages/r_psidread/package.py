# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsidread(RPackage):
	"""Streamline Building Panel Data from Panel Study of Income
Dynamics ('PSID') Raw Files

	Streamline the management, creation, and formatting of panel data from the Panel Study of Income Dynamics ('PSID') <https://psidonline.isr.umich.edu> using this user-friendly tool. Simply define variable names and input code book details directly from the 'PSID' official website, and this toolbox will efficiently facilitate the data preparation process, transforming raw 'PSID' files into a well-organized format ready for further analysis.
	"""
	
	homepage = "https://github.com/Qcrates/psidread"
	cran = "psidread" 

	version("1.0.3", md5="3b98609c1a0a2110acadf68ffb5e095e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-asciisetupreader", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
