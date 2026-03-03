# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcarb(RPackage):
	"""Dose Rate Modelling of Carbonate-Rich Samples

	Translation of the 'MATLAB' program 'Carb' (Nathan and Mauz 2008 <DOI:10.1016/j.radmeas.2007.12.012>; Mauz and Hoffmann 2014) for dose rate modelling for carbonate-rich samples in the context of trapped charged dating (e.g., luminescence dating) applications. 
	"""
	
	homepage = "https://r-lum.github.io/RCarb/"
	cran = "RCarb" 

	version("0.1.6", md5="b2bdf338fd3754398d335acc6eb48469")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-interp@1.1:", type=("build", "run"))
	depends_on("r-matrixstats@0.62:", type=("build", "run"))
