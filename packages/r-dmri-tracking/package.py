# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmriTracking(RPackage):
	"""DiST - Diffusion Direction Smoothing and Tracking

	It provides functions to apply the deterministic tracking algorithm - DiST (Wong et al 2016) <doi:10.1214/15-AOAS880> and to plot tractography results.
	"""
	
	homepage = "https://github.com/vic-dragon/dmri.tracking"
	cran = "dmri.tracking" 

	version("0.1.0", md5="b38663de1140f10491a5264caf0ed399")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
