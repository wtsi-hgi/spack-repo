# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquatags(RPackage):
	"""Equations to 'XML'

	Provides function to transform latex math expressions 
 into format 'HTML' or 'Office Open XML Math'. The 'XML' 
 result can then be included in 'HTML', 'Microsoft Word' 
 documents or 'Microsoft PowerPoint' presentations by using 
 a 'Markdown' document or the R package 'officer'. 
	"""
	
	cran = "equatags" 

	version("0.2.0", md5="8913703fe72ed1d3909e2a27a8a0370f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xslt", type=("build", "run"))
	depends_on("r-katex", type=("build", "run"))
