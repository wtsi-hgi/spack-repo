# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsstda(RPackage):
	"""Gene Structure Survival using Topological Data Analysis

	Mapper-based survival analysis with transcriptomics data is designed to carry out. 
			Mapper-based survival analysis is a modification of Progression Analysis of Disease (PAD) 
			where survival data is taken into account in the filtering function. More 
			details in: J. Fores-Martos, B. Suay-Garcia, R. Bosch-Romeu, M.C. Sanfeliu-Alonso, 
			A. Falco, J. Climent, "Progression Analysis of Disease with Survival (PAD-S) by SurvMap 
			identifies different prognostic subgroups of breast cancer in a large combined set of transcriptomics
			and methylation studies" <doi:10.1101/2022.09.08.507080>.
	"""
	
	cran = "GSSTDA" 

	version("0.1.3", md5="fba8f20b28c78cbdb61e0f4104ce5f28")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
