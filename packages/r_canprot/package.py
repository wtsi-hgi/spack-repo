# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanprot(RPackage):
	"""Chemical Analysis of Proteins

	Chemical analysis of proteins based on their amino acid
  compositions. Amino acid compositions can be read from FASTA files and used to
  calculate chemical metrics including carbon oxidation state and stoichiometric
  hydration state, as described in Dick et al. (2020) <doi:10.5194/bg-17-6145-2020>. 
  Other properties that can be calculated include protein length, grand average of
  hydropathy (GRAVY), isoelectric point (pI), molecular weight (MW), standard
  molal volume (V0), and metabolic costs (Akashi and Gojobori, 2002
  <doi:10.1073/pnas.062526999>; Wagner, 2005 <doi:10.1093/molbev/msi126>;
  Zhang et al., 2018 <doi:10.1038/s41467-018-06461-1>). A database of amino acid
  compositions of human proteins derived from UniProt is provided.
	"""
	
	homepage = "https://github.com/jedick/canprot"
	cran = "canprot" 

	version("2.0.0", md5="baca332d4f24958a087e2a48900567ee")
	version("1.1.2", md5="8a552a0f3339970e4281b736104ac2ea")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-chnosz@1.3.2:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
