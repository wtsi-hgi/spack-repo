# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHlar(RPackage):
	"""Tools for HLA Data

	A streamlined tool for eplet analysis of donor and recipient HLA (human leukocyte antigen) mismatch. Messy, low-resolution HLA typing data is cleaned, and imputed to high-resolution using the NMDP (National Marrow Donor Program) haplotype reference database <https://haplostats.org/haplostats>. High resolution data is analyzed for overall or single antigen eplet mismatch using a reference table (currently supporting 'HLAMatchMaker' <http://www.epitopes.net> versions 2 and 3). Data can enter or exit the workflow at different points depending on the user's aims and initial data quality.
	"""
	
	homepage = "https://pubmed.ncbi.nlm.nih.gov/35101308/"
	cran = "hlaR" 

	version("1.0.0", md5="bffce74bae8888def8a79016970c1fde")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-schoolmath", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
