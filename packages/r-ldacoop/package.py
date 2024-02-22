# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdacoop(RPackage):
	"""Analysis of Data from Limiting Dilution Assay (LDA) with or
without Cellular Cooperation

	Cellular cooperation compromises the established method of
	calculating clonogenic activity from limiting dilution assay (LDA) data.
	This tool provides functions that enable robust analysis in presence or
	absence of cellular cooperation. The implemented method incorporates the
	same cooperativity module to model the non-linearity associated with
	cellular cooperation as known from the colony formation assay (Brix et al.
	(2021) <doi:10.1038/s41596-021-00615-0>: "Analysis of clonogenic growth in
	vitro." Nature protocols).
	"""
	
	homepage = "https://github.com/ZytoHMGU/LDAcoop"
	cran = "LDAcoop" 

	version("0.1.1", md5="84d1a00bfe3980ebeebd8517b0345744")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
