# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeggdzpathwaysgeo(RPackage):
	"""KEGG Disease Datasets from GEO

	This is a collection of 24 data sets for which the phenotype is a disease with a corresponding pathway in the KEGG database.This collection of datasets were used as gold standard in comparing gene set analysis methods by the PADOG package.
	"""
	
	bioc = "KEGGdzPathwaysGEO"

	version("1.46.0", commit="3b4f21ae7c25d978853d6eb87fa99c630f7cbe9d")
	version("1.40.0", commit="578b101e1d645910b878e9f263b25206ff7dce0a")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

