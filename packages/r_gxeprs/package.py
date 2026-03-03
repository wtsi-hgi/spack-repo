# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGxeprs(RPackage):
	"""Genotype-by-Environment Interaction in Polygenic Score Models

	A novel PRS model is introduced to enhance the prediction accuracy by utilising GxE effects. This package performs Genome Wide Association Studies (GWAS) and Genome Wide Environment Interaction Studies (GWEIS) using a discovery dataset. The package has the ability to obtain polygenic risk scores (PRSs) for a target sample. Finally it predicts the risk values of each individual in the target sample. Users have the choice of using existing models (Li et al., 2015) <doi:10.1093/annonc/mdu565>, (Pandis et al., 2013) <doi:10.1093/ejo/cjt054>, (Peyrot et al., 2018) <doi:10.1016/j.biopsych.2017.09.009> and (Song et al., 2022) <doi:10.1038/s41467-022-32407-9>, as well as newly proposed models for genomic risk prediction (refer to the URL for more details).
	"""
	
	homepage = "https://github.com/DoviniJ/GxEprs"
	cran = "GxEprs" 

	version("1.1", md5="5384310b46404156ae3eec09fe608b01")

	depends_on("r@2.10:", type=("build", "run"))
