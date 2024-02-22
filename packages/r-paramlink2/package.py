# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParamlink2(RPackage):
	"""Parametric Linkage Analysis

	Parametric linkage analysis of monogenic traits in medical
    pedigrees. Features include singlepoint analysis, multipoint analysis
    via 'MERLIN' (Abecasis et al. (2002) <doi:10.1038/ng786>),
    visualisation of log of the odds (LOD) scores and summaries of linkage
    peaks. Disease models may be specified to accommodate phenocopies,
    reduced penetrance and liability classes. 'paramlink2' is part of the
    'ped suite' package ecosystem, presented in 'Pedigree Analysis in R'
    (Vigeland, 2021, ISBN:9780128244302).
	"""
	
	homepage = "https://github.com/magnusdv/paramlink2"
	cran = "paramlink2" 

	version("1.0.4", md5="5581610bcc8c87ae3001a107b21767cf", url="https://cran.r-project.org/src/contrib/paramlink2_1.0.4.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-pedtools", type=("build", "run"))
	depends_on("r-pedprobr", type=("build", "run"))
