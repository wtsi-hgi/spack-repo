# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTuwmodel(RPackage):
	"""Lumped/Semi-Distributed Hydrological Model for Education
Purposes

	The model, developed at the Vienna University of Technology, is a lumped conceptual rainfall-runoff model, following the structure of the HBV model. 
             The model can also be run in a semi-distributed fashion and with dual representation of soil layer.
             The model runs on a daily or shorter time step and consists of a snow routine, a soil moisture routine and a flow routing routine. 
             See Parajka, J., R. Merz, G. Bloeschl (2007) <DOI:10.1002/hyp.6253> Uncertainty and multiple objective calibration in regional water balance modelling: case study in 320 Austrian catchments, Hydrological Processes, 21, 435-446. 
	"""
	
	cran = "TUWmodel" 

	version("1.1-1", md5="a2f2f826e65734d6b405f1c94c283c8f")

	depends_on("r@3:", type=("build", "run"))
