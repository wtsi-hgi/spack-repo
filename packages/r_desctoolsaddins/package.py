# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesctoolsaddins(RPackage):
	"""Interactive Functions to be Used as Shortcuts in 'RStudio'

	'RStudio' as of recently offers the option to define addins and assign shortcuts to them. This package contains addins for a few most frequently used functions in a data scientist's (at least mine) daily work (like str(), example(), plot(), head(), view(), Desc()). Most of these functions will use the current selection in the editor window and send the specific command to the console while instantly executing it. Assigning shortcuts to these addins will save you quite a few keystrokes.
	"""
	
	homepage = "https://github.com/AndriSignorell/DescToolsAddIns/"
	cran = "DescToolsAddIns" 

	version("1.10", md5="20b32cbe391df5d726480bdde2d4720e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-desctools@0.99.30:", type=("build", "run"))
	depends_on("r-rstudioapi@0.1:", type=("build", "run"))
	depends_on("r-manipulate", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
