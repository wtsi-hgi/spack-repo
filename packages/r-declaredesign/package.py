# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeclaredesign(RPackage):
	"""Declare and Diagnose Research Designs

	Researchers can characterize and learn about the properties of
    research designs before implementation using `DeclareDesign`. Ex ante
    declaration and diagnosis of designs can help researchers clarify the 
    strengths and limitations of their designs and to improve their 
    properties, and can help readers evaluate a research strategy prior
    to implementation and without access to results. It can also make it
    easier for designs to be shared, replicated, and critiqued.
	"""
	
	homepage = "https://declaredesign.org/r/declaredesign/"
	cran = "DeclareDesign" 

	version("1.0.8", md5="4a2dc1761071fa896367dced21eaa648")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-randomizr@0.20:", type=("build", "run"))
	depends_on("r-fabricatr@0.10:", type=("build", "run"))
	depends_on("r-estimatr@0.20:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
