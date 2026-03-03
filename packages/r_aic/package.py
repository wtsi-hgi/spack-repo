# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAic(RPackage):
	"""Testing for Compositional Pathologies in Datasets

	A set of tests for compositional pathologies. Tests for coherence of correlations with aIc.coherent() as suggested by (Erb et al. (2020) <doi:10.1016/j.acags.2020.100026>),  compositional dominance of distance with aIc.dominant(), compositional perturbation invariance with aIc.perturb() as suggested by (Aitchison (1992) <doi:10.1007/BF00891269>) and singularity of the covariation matrix with aIc.singular(). Currently tests five data transformations: prop, clr, TMM, TMMwsp, and RLE from the R packages 'ALDEx2', 'edgeR' and 'DESeq2' (Fernandes et al (2014) <doi:10.1186/2049-2618-2-15>, Anders et al. (2013)<doi:10.1038/nprot.2013.099>).
	"""
	
	homepage = "https://github.com/ggloor/aIc"
	cran = "aIc" 

	version("1.0", md5="dda4130ca1119183fd1b52ec02773b49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-zcompositions", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-aldex2", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
