# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanaffydata(RPackage):
	"""GEO accession GSE64985 and ArrayExpress accession E-MTAB-62 as ExpressionSet objects

	Re-analysis of human gene expression data generated on the Affymetrix HG_U133PlusV2 (EH176) and Affymetrix HG_U133A (EH177) platforms. The original data were normalized using robust multiarray averaging (RMA) to obtain an integrated gene expression atlas across diverse biological sample types and conditions. The entire compendia comprisee 9395 arrays for EH176 and 5372 arrays for EH177.
	"""
	
	bioc = "HumanAffyData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/HumanAffyData_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/HumanAffyData/HumanAffyData_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="202bec80cd244e90b2ab3362682b9db18c2c9c1c284e2d7b02c5f02641b6443c")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))

