# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPssim(RPackage):
	"""Test of Independence & Image Structural Similarity Measure PSSIM

	Test-based Image structural similarity measure and test of independence. 
    This package implements the key functions of two tasks: (1) computing
    image structural similarity measure PSSIM of Wang, Maldonado and
    Silwal (2011) <DOI:10.1016/j.csda.2011.04.021>;
    and (2) test of independence between a response and 
    a covariate in presence of heteroscedastic treatment effects 
    proposed by Wang, Tolos, and Wang (2010) <DOI:10.1002/cjs.10068>.
	"""
	
	cran = "PSSIM" 

	version("0.1.0", md5="85120ffda964ecf8d3bda2c0105bab37")

	depends_on("r@3.5:", type=("build", "run"))
