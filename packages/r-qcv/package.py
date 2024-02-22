# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcv(RPackage):
	"""Quantifying Construct Validity

	Primarily, the 'qcv' package computes key indices related to the Quantifying Construct
    Validity procedure (QCV; Westen & Rosenthal, 2003 <doi:10.1037/0022-3514.84.3.608>; 
    see also Furr & Heuckeroth, in press). The qcv() function is the heart of the 'qcv' package, 
    but additional functions in the package provide useful ancillary information related to the QCV procedure.
	"""
	
	cran = "qcv" 

	version("1.0", md5="a9e62ac7c1b807319bb5bff67a41e5c6")

	depends_on("r@3.5.1:", type=("build", "run"))
