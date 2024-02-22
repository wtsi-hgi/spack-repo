# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRibench(RPackage):
	"""Benchmark Suite for Indirect Methods for RI Estimation

	The provided benchmark suite enables the automated evaluation and comparison of any existing and novel indirect method for reference interval ('RI') estimation in a systematic way.
	Indirect methods take routine measurements of diagnostic tests, containing pathological and non-pathological samples as input and use sophisticated
	statistical methods to derive a model describing the distribution of the non-pathological samples, which can then be 
	used to derive reference intervals. The benchmark suite contains 5,760 simulated test sets with varying difficulty.
	To include any indirect method, a custom wrapper function needs to be provided. 
	The package offers functions for generating the test sets, executing the indirect method and evaluating the results.
	See ?RIbench or vignette("RIbench_package") for a more comprehensive description of the features. 
	A detailed description and application is described in Ammer T., Schuetzenmeister A., Prokosch H.-U., Zierk J., Rank C.M., Rauh M. "RIbench: A Proposed Benchmark for the Standardized Evaluation of Indirect Methods for Reference Interval Estimation". Clinical Chemistry (2022) <doi:10.1093/clinchem/hvac142>.  
	"""
	
	cran = "RIbench" 

	version("1.0.2", md5="6d5b281539226209f2e52d3158d708b1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-optparse", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
