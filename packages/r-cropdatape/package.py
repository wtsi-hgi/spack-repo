# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCropdatape(RPackage):
	"""Open Data of Agricultural Production of Crops of Peru

	Provides peruvian agricultural production data from the Agriculture Minestry of Peru (MINAGRI). The first version includes
             6 crops: rice, quinoa, potato, sweet potato, tomato and wheat; all of them across 24 departments. Initially,  in excel files which has been transformed
             and assembled using tidy data principles, i.e. each variable is in a column, each observation is a row and each value is in a cell.
             The variables variables are sowing and harvest area per crop, yield, production and price per plot, every one year, from 2004 to 2014.
	"""
	
	homepage = "https://github.com/omarbenites/cropdatape"
	cran = "cropdatape" 

	version("1.0.0", md5="5fe45899246babf07964eba0b81f4214")

	depends_on("r@3.3.1:", type=("build", "run"))
