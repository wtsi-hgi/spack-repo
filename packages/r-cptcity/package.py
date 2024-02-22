# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCptcity(RPackage):
	"""'cpt-city' Colour Gradients

	Incorporates colour gradients from the 'cpt-city' web archive available at <http://soliton.vm.bytemark.co.uk/pub/cpt-city/>. 
	"""
	
	homepage = "https://github.com/ibarraespinosa/cptcity"
	cran = "cptcity" 

	version("1.0.6", md5="c9fc6c4d5a5c561671bec29db493cdd5")

	depends_on("r@2.10:", type=("build", "run"))
