# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacarron(RPackage):
	"""Prioritization of potentially bioactive metabolic features from epidemiological and environmental metabolomics datasets

	Macarron is a workflow for the prioritization of potentially bioactive metabolites from metabolomics experiments. Prioritization integrates strengths of evidences of bioactivity such as covariation with a known metabolite, abundance relative to a known metabolite and association with an environmental or phenotypic indicator of bioactivity. Broadly, the workflow consists of stratified clustering of metabolic spectral features which co-vary in abundance in a condition, transfer of functional annotations, estimation of relative abundance and differential abundance analysis to identify associations between features and phenotype/condition.
	"""
	
	homepage = "http://huttenhower.sph.harvard.edu/macarron"
	bioc = "Macarron"

	version("1.12.2", commit="33ab0482144846393361eed1c632f87409feb07b")
	version("1.6.0", commit="3120897e1898a0577b9d6aa1cba44616384ab42e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-maaslin2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-logging", type=("build", "run"))
