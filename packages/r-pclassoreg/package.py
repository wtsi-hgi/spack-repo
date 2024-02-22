# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPclassoreg(RPackage):
	"""Group Regression Models for Risk Protein Complex Identification

	Two protein complex-based group regression models (PCLasso and PCLasso2) for risk protein complex identification. PCLasso is a prognostic model that identifies risk protein complexes associated with survival. PCLasso2 is a classification model that identifies risk protein complexes associated with classes. For more information, see Wang and Liu (2021) <doi:10.1093/bib/bbab212>. 
	"""
	
	homepage = "https://github.com/weiliu123/PCLassoReg"
	cran = "PCLassoReg" 

	version("1.0.0", md5="70048cb7952bf948448ac08cda2a5041")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
