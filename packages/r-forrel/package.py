# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForrel(RPackage):
	"""Forensic Pedigree Analysis and Relatedness Inference

	Forensic applications of pedigree analysis, including
    likelihood ratios for relationship testing, general relatedness
    inference, marker simulation, and power analysis. 'forrel' is part of
    the 'pedsuite', a collection of packages for pedigree analysis,
    further described in the book 'Pedigree Analysis in R' (Vigeland,
    2021, ISBN:9780128244302). Several functions deal specifically with
    power analysis in missing person cases, implementing methods described
    in Vigeland et al. (2020) <doi:10.1016/j.fsigen.2020.102376>. Data
    import from the 'Familias' software (Egeland et al. (2000)
    <doi:10.1016/S0379-0738(00)00147-X>) is supported through the
    'pedFamilias' package.
	"""
	
	homepage = "https://github.com/magnusdv/forrel"
	cran = "forrel" 

	version("1.6.1", md5="64a72a0fafc711ccd8a125f6318ffecd")

	depends_on("r-pedtools@2.2:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pedfamilias", type=("build", "run"))
	depends_on("r-pedprobr@0.8:", type=("build", "run"))
	depends_on("r-ribd@1.5:", type=("build", "run"))
