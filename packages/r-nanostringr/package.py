# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanostringr(RPackage):
	"""Performs Quality Control, Data Normalization, and Batch Effect
Correction for 'NanoString nCounter' Data

	Provides quality control (QC), normalization, and batch
    effect correction operations for 'NanoString nCounter' data, Talhouk
    et al. (2016) <doi:10.1371/journal.pone.0153844>.  Various metrics are
    used to determine which samples passed or failed QC.  Gene expression
    should first be normalized to housekeeping genes, before a
    reference-based approach is used to adjust for batch effects.  Raw
    NanoString data can be imported in the form of Reporter Code Count
    (RCC) files.
	"""
	
	homepage = "https://github.com/TalhoukLab/nanostringr/"
	cran = "nanostringr" 

	version("0.4.1", md5="9f32f2da9746ee570f5736dbe68483bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ccapp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
