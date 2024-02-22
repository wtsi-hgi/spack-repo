# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmr(RPackage):
	"""Analysis of Cardiac Magnetic Resonance Images

	Computes maximum response from Cardiac Magnetic Resonance Images using spatial and voxel wise spline based Bayesian model. This is an implementation of the methods described in Schmid (2011) <doi:10.1109/TMI.2011.2109733> "Voxel-Based Adaptive Spatio-Temporal Modelling of Perfusion Cardiovascular MRI". IEEE TMI 30(7) p. 1305 - 1313.
	"""
	
	homepage = "https://bioimaginggroup.github.io/cmr/"
	cran = "cmR" 

	version("1.1", md5="20dd96f5887e0b12bec92d9749e8ff8a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
