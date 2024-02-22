# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMefa(RPackage):
	"""Multivariate Data Handling in Ecology and Biogeography

	A framework package aimed to provide standardized computational environment for specialist work via object classes to represent the data coded by samples, taxa and segments (i.e. subpopulations, repeated measures). It supports easy processing of the data along with cross tabulation and relational data tables for samples and taxa. An object of class `mefa' is a project specific compendium of the data and can be easily used in further analyses. Methods are provided for extraction, aggregation, conversion, plotting, summary and reporting of `mefa' objects. Reports can be generated in plain text or LaTeX format. Vignette contains worked examples.
	"""
	
	homepage = "https://github.com/psolymos/mefa"
	cran = "mefa" 

	version("3.2-8", md5="c6ab090090a592167dd5ead38703e19b")

	depends_on("r@2.14:", type=("build", "run"))
