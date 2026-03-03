# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemminedrugs(RPackage):
	"""DrugBank data set

	An annotation package for use with ChemmineR. This package includes data from DrugBank. DUD data can be downloaded using the "DUD()" function in ChemmineR.
	"""
	
	bioc = "ChemmineDrugs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ChemmineDrugs_1.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ChemmineDrugs/ChemmineDrugs_1.0.2.tar.gz"]

	version("1.0.2", md5="2a3646e5173e93080fb5b49564f5d545")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))

