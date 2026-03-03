# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilest(RPackage):
	"""Fine-Level Structure Simulator

	A population genetic simulator, which is able to generate synthetic datasets for single-nucleotide polymorphisms (SNP) for multiple populations. The genetic distances among populations can be set according to the Fixation Index (Fst) as explained in Balding and Nichols (1995) <doi:10.1007/BF01441146>. This tool is able to simulate outlying individuals and missing SNPs can be specified. For Genome-wide association study (GWAS), disease status can be set in desired level according risk ratio.
	"""
	
	homepage = "https://gitlab.com/kris.ccp/filest"
	cran = "FILEST" 

	version("1.1.2", md5="5e252edb1a0fe83b9c6a406b1679c7c6")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-kris@1.1.1:", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
