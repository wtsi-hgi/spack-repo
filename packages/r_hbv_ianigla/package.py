# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHbvIanigla(RPackage):
	"""Modular Hydrological Model

	The HBV hydrological model (Bergström, S. and Lindström, G., (2015) <doi:10.1002/hyp.10510>) has been split in modules to allow the user to build his/her own model. This version was developed by the author in IANIGLA-CONICET (Instituto Argentino de Nivologia, Glaciologia y Ciencias Ambientales - Consejo Nacional de Investigaciones Cientificas y Tecnicas) for hydroclimatic studies in the Andes. HBV.IANIGLA incorporates routines for clean and debris covered glacier melt simulations. 
	"""
	
	homepage = "https://gitlab.com/ezetoum27/hbv.ianigla"
	cran = "HBV.IANIGLA" 

	version("0.2.6", md5="3d656aa1e1c9fb35079ac21417569454")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
