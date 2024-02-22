# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtsea(RPackage):
	"""Drug Target Set Enrichment Analysis

	It is a novel tool used to identify the candidate drugs against a particular disease based on the drug target set enrichment analysis. It assumes the most effective drugs are those with a closer affinity in the protein-protein interaction network to the specified disease. (See Gómez-Carballa et al. (2022) <doi: 10.1016/j.envres.2022.112890> and Feng et al. (2022) <doi: 10.7150/ijms.67815> for disease expression profiles; see Wishart et al. (2018) <doi: 10.1093/nar/gkx1037> and Gaulton et al. (2017) <doi: 10.1093/nar/gkw1074> for drug target information; see Kanehisa et al. (2021) <doi: 10.1093/nar/gkaa970> for the details of KEGG database.)
	"""
	
	cran = "DTSEA" 

	version("0.0.3", md5="8359670addb4ec7ea38d26baccc9ec6e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
