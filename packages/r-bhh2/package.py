# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhh2(RPackage):
	"""Useful Functions for Box, Hunter and Hunter II

	Functions and data sets reproducing some examples in
             Box, Hunter and Hunter II.  Useful for statistical design
             of experiments, especially factorial experiments.  
	"""
	
	cran = "BHH2" 

	version("2016.05.31", md5="134ce7653488e1881e7fb894fa7256ca", url="https://cran.r-project.org/src/contrib/BHH2_2016.05.31.tar.gz")

	depends_on("r@2:", type=("build", "run"))
