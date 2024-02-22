# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfd(RPackage):
	"""Extract Drugs from Differential Expression Data from LINCS
Database

	Get Drug information from given differential expression profile. The package search for the bioactive compounds from reference databases such as LINCS containing the genome-wide gene expression signature (GES) from tens of thousands of drug and genetic perturbations (Subramanian et al. (2017) <DOI:10.1016/j.cell.2017.10.049>).
	"""
	
	homepage = "https://github.com/MohmedSoudy/DFD"
	cran = "DFD" 

	version("0.1.0", md5="cb69ff57334dc619fb65f273900192de")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gprofiler2", type=("build", "run"))
	depends_on("r-signaturesearch", type=("build", "run"))
	depends_on("r-signaturesearchdata", type=("build", "run"))
