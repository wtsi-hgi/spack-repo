# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHybriddesign(RPackage):
	"""Hybrid Design for Phase I Dose-Finding Studies

	The Hybrid design is a combination of model-assisted design (e.g., the modified 
             Toxicity Probability Interval design) with dose-toxicity model-based design for 
             phase I dose-finding studies. The hybrid design controls the overdosing 
             toxicity well and leads to a recommended dose closer to the true maximum tolerated 
             dose (MTD) due to its ability to calibrate for an intermediate dose. More details 
             can be found in Liao et al. 2022 <doi:10.1002/ijc.34203>.
	"""
	
	cran = "HybridDesign" 

	version("1.0", md5="07f53fed8f2143b333d4bb9966901e80")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-testit", type=("build", "run"))
	depends_on("r-resourceselection", type=("build", "run"))
