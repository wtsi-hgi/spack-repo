# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGapDatasets(RPackage):
	"""Datasets for 'gap'

	Datasets associated with the 'gap' package. Currently,
             it includes an example data for regional association
             plot (CDKN), an example data for a genomewide association
             meta-analysis (OPG), data in studies of Parkinson's diease (PD),
             ALHD2 markers and alcoholism (aldh2), APOE/APOC1 markers
             and Schizophrenia (apoeapoc), cystic fibrosis (cf), a
             Olink/INF panel (inf1), Manhattan plots with (hr1420, mhtdata)
             and without (w4) gene annotations.
	"""
	
	homepage = "https://jinghuazhao.github.io/R/"
	cran = "gap.datasets" 

	version("0.0.6", md5="7c698fe9b41dea20f52ee5184f36b269")

	depends_on("r@2.10:", type=("build", "run"))
