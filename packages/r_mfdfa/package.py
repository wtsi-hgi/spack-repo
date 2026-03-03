# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfdfa(RPackage):
	"""MultiFractal Detrended Fluctuation Analysis

	Contains the MultiFractal Detrended Fluctuation Analysis (MFDFA), 
  MultiFractal Detrended Cross-Correlation Analysis (MFXDFA), and the Multiscale
  Multifractal Analysis (MMA). The MFDFA() function proposed in this package was 
  used in Laib et al. (<doi:10.1016/j.chaos.2018.02.024> and <doi:10.1063/1.5022737>). 
  See references for more information. Interested users can find a parallel version of
  the MFDFA() function on GitHub.
	"""
	
	homepage = "https://mlaib.github.io"
	cran = "MFDFA" 

	version("1.1", md5="a8ade56a6d9d9911cb22569a8263ffd4")

	depends_on("r-numbers", type=("build", "run"))
