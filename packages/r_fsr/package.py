# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsr(RPackage):
	"""Handling Fuzzy Spatial Data

	Support for fuzzy spatial objects, their operations, and fuzzy spatial inference models based on Spatial Plateau Algebra. 
    It employs fuzzy set theory and fuzzy logic as foundation to deal with spatial fuzziness. 
    It mainly implements underlying concepts defined in the following research papers: 
    (i) "Spatial Plateau Algebra: An Executable Type System for Fuzzy Spatial Data Types" <doi:10.1109/FUZZ-IEEE.2018.8491565>; 
    (ii) "A Systematic Approach to Creating Fuzzy Region Objects from Real Spatial Data Sets" <doi:10.1109/FUZZ-IEEE.2019.8858878>; 
    (iii) "Spatial Data Types for Heterogeneously Structured Fuzzy Spatial Collections and Compositions" <doi:10.1109/FUZZ48607.2020.9177620>;
    (iv) "Fuzzy Inference on Fuzzy Spatial Objects (FIFUS) for Spatial Decision Support Systems" <doi:10.1109/FUZZ-IEEE.2017.8015707>;
    (v) "Evaluating Region Inference Methods by Using Fuzzy Spatial Inference Models" <doi:10.1109/FUZZ-IEEE55066.2022.9882658>.
	"""
	
	homepage = "https://accarniel.github.io/fsr/"
	cran = "fsr" 

	version("2.0.1", md5="381720464b0367fab03c876e5c695a0c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-sf@1.0.15:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-pso@1.0.3:", type=("build", "run"))
	depends_on("r-e1071@1.7.3:", type=("build", "run"))
