# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWallomicsdata(RPackage):
	"""Datasets for Multi-Omics Integration in a Plant Abiotic Stress
Context

	Datasets from the WallOmics project. Contains phenomics, metabolomics, proteomics and transcriptomics data collected from two organs of five ecotypes of the model plant Arabidopsis thaliana exposed to two temperature growth conditions. Exploratory and integrative analyses of these data are presented in Durufle et al (2020) <doi:10.1093/bib/bbaa166> and Durufle et al (2020) <doi:10.3390/cells9102249>.
	"""
	
	cran = "WallomicsData" 

	version("1.0", md5="9a0d834790a093e25a2b669ee3e487b4")

	depends_on("r@2.10:", type=("build", "run"))
