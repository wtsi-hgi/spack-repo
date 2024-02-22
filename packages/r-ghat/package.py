# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhat(RPackage):
	"""Quantifying Evolution and Selection on Complex Traits

	Functions are provided for quantifying evolution and selection on complex traits. 
              The package implements effective handling and analysis algorithms scaled for 
              genome-wide data and calculates a composite statistic, denoted Ghat, which is used 
              to test for selection on a trait. The package provides a number of simple examples 
              for handling and analysing the genome data and visualising the output and results. 
              Beissinger et al., (2018) <doi:10.1534/genetics.118.300857>.
	"""
	
	homepage = "https://academic.oup.com/genetics/article/209/1/321/5931021"
	cran = "Ghat" 

	version("0.2.0", md5="cd8143e694a00f68b35dae1097614b31")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rrblup", type=("build", "run"))
