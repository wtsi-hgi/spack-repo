# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomizr(RPackage):
	"""Easy-to-Use Tools for Common Forms of Random Assignment and
Sampling

	Generates random assignments for common experimental designs and 
	    random samples for common sampling designs.
	"""
	
	homepage = "https://declaredesign.org/r/randomizr/"
	cran = "randomizr" 

	version("1.0.0", md5="7860c9a6c26008f6d4ebbcfc01ce911b")

	depends_on("r@3.5:", type=("build", "run"))
