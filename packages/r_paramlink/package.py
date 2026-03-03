# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParamlink(RPackage):
	"""Parametric Linkage and Other Pedigree Analysis in R

	NOTE: 'PARAMLINK' HAS BEEN SUPERSEDED BY THE 'PED SUITE'
    PACKAGES (<https://magnusdv.github.io/pedsuite/>). 'PARAMLINK' IS
    MAINTAINED ONLY FOR LEGACY PURPOSES AND SHOULD NOT BE USED IN NEW
    PROJECTS. A suite of tools for analysing pedigrees with marker data,
    including parametric linkage analysis, forensic computations,
    relatedness analysis and marker simulations. The core of the package
    is an implementation of the Elston-Stewart algorithm for pedigree
    likelihoods, extended to allow mutations as well as complex
    inbreeding. Features for linkage analysis include singlepoint LOD
    scores, power analysis, and multipoint analysis (the latter through a
    wrapper to the 'MERLIN' software). Forensic applications include
    exclusion probabilities, genotype distributions and conditional
    simulations. Data from the 'Familias' software can be imported and
    analysed in 'paramlink'. Finally, 'paramlink' offers many utility
    functions for creating, manipulating and plotting pedigrees with or
    without marker data (the actual plotting is done by the 'kinship2'
    package).
	"""
	
	homepage = "https://github.com/magnusdv/paramlink"
	cran = "paramlink" 

	version("1.1-5", md5="0a5ce8ec61966c520872102604195fe5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
