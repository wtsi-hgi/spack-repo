# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrogeo(RPackage):
	"""Groundwater Data Presentation and Interpretation

	Contains one function for drawing Piper diagrams (also
    called Piper-Hill diagrams) of water analyses for major ions.
	"""
	
	homepage = "http://rockhead.biz"
	cran = "hydrogeo" 

	version("0.6-1", md5="a9df2e9f0c2932f341867db6945bbdc8")

	depends_on("r@2.6:", type=("build", "run"))
