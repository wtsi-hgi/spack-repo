# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrimr(RPackage):
	"""Calculate Optical Parameters from Spindle Stage Measurements

	Calculates optical parameters of crystals like the optical
    axes, the axis angle 2V, and the direction of the principal axes of
    the indicatrix from extinction angles measured on a spindle stage 
    mounted on a polarisation microscope stage. Details of the method can be found in Dufey (2017) <arXiv:1703.00070>. 
	"""
	
	cran = "GrimR" 

	version("0.5", md5="ef2aaf452c152a5a83acfd6e30079f36")

	depends_on("r-car", type=("build", "run"))
