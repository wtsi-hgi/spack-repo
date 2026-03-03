# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdft(RPackage):
	"""Downscaling and Bias Correction via Non-Parametric CDF-Transform

	Statistical downscaling and bias correction (model output statistics) method based on cumulative distribution functions (CDF) transformation. See Michelangeli, Vrac, Loukos (2009) Probabilistic downscaling approaches: Application to wind cumulative distribution functions. Geophysical Research Letters, 36, L11708, <doi:10.1029/2009GL038401>. ; and Vrac, Drobinski, Merlo, Herrmann, Lavaysse, Li, Somot (2012) Dynamical and statistical downscaling of the French Mediterranean climate: uncertainty assessment. Nat. Hazards Earth Syst. Sci., 12, 2769-2784, www.nat-hazards-earth-syst-sci.net/12/2769/2012/, <doi:10.5194/nhess-12-2769-2012>.
	"""
	
	cran = "CDFt" 

	version("1.2", md5="22c933028acbd9614ee76885c6cab648")

	depends_on("r@1.8:", type=("build", "run"))
