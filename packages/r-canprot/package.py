# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanprot(RPackage):
	"""Chemical Metrics of Differentially Expressed Proteins

	Chemical metrics of differentially expressed proteins in cancer
  and cell culture proteomics experiments. Data files in the package have amino
  acid compositions of proteins obtained from UniProt and >250 published lists of
  up- and down-regulated proteins in different cancer types and laboratory
  experiments. Functions are provided to calculate chemical metrics including
  protein length, grand average of hydropathicity (GRAVY), isoelectric point
  (pI), carbon oxidation state, and stoichiometric hydration state; the latter
  two are described in Dick et al. (2020) <doi:10.5194/bg-17-6145-2020>. The
  vignettes visualize differences of chemical metrics between up- and
  down-regulated proteins and list literature references for all datasets.
	"""
	
	homepage = "https://github.com/jedick/canprot"
	cran = "canprot" 

	version("1.1.2", md5="8a552a0f3339970e4281b736104ac2ea")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-chnosz@1.3.2:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
