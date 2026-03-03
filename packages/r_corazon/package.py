# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorazon(RPackage):
	"""Apply 'colorffy' Color Gradients Within 'shiny' Elements

	Allows the user to apply nice color gradients to 'shiny' elements.
    The gradients are extracted from the 'colorffy' website. See <https://www.colorffy.com/gradients/catalog>.
	"""
	
	homepage = "https://github.com/feddelegrand7/corazon"
	cran = "corazon" 

	version("0.1.0", md5="31e9d037985021f8c3b344e1fb7500b3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
