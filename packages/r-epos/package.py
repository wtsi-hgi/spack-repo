# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpos(RPackage):
	"""Epilepsy Ontologies' Similarities

	Analysis and visualization of similarities between epilepsy ontologies based on text mining results by comparing ranked lists of co-occurring drug terms in the BioASQ corpus. The ranked result lists of neurological drug terms co-occurring with terms from the epilepsy ontologies EpSO, ESSO, EPILONT, EPISEM and FENICS undergo further analysis. The source data to create the ranked lists of drug names is produced using the text mining workflows described in Mueller, Bernd and Hagelstein, Alexandra (2016) <doi:10.4126/FRL01-006408558>, Mueller, Bernd et al. (2017) <doi:10.1007/978-3-319-58694-6_22> and Mueller, Bernd and Rebholz-Schuhmann, Dietrich (2020) <doi:10.1007/978-3-030-43887-6_52>.
	"""
	
	cran = "epos" 

	version("1.0", md5="2720b541b780dc022e54edd1ef2c0ba5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-topklists", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mongolite", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
