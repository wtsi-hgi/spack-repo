# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrouptest(RPackage):
	"""Multiple Testing Procedure for Grouped Hypotheses

	Contains functions for a two-stage multiple testing procedure for grouped hypothesis, aiming at controlling both the total posterior false discovery rate and within-group false discovery rate. 
	"""
	
	cran = "GroupTest" 

	version("1.0.1", md5="101893faa77070fab1353f2df72271ef")

