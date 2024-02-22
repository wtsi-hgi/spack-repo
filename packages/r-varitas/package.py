# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVaritas(RPackage):
	"""Variant Calling in Targeted Analysis Sequencing Data

	Multi-caller variant analysis pipeline for targeted analysis sequencing (TAS) data. Features a modular, automated workflow that can start with raw reads and produces a user-friendly PDF summary and a spreadsheet containing consensus variant information.
	"""
	
	cran = "varitas" 

	version("0.0.2", md5="9ea2d8878d141c7dd73672febdeb976c")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
	depends_on("bedtools2@2.27.1:", type=("build", "link", "run"))
	depends_on("bwa", type=("build", "link", "run"))
