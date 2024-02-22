# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCornerstoner(RPackage):
	"""Collection of Scripts for Interface Between 'Cornerstone' and
'R'

	Collection of generic 'R' scripts which enable you to use existing 'R' routines in 'Cornerstone'.

          The desktop application 'Cornerstone' (<https://www.camline.com/en/products/cornerstone/cornerstone-core.html>)
    is a data analysis software provided by 'camLine' that empowers engineering teams to find solutions even faster.
    The engineers incorporate intensified hands-on statistics into their projects.
    They benefit from an intuitive and uniquely designed graphical Workmap concept: you design
    experiments (DoE) and explore data, analyze dependencies, and find answers you can act upon,
    immediately, interactively, and without any programming.

          While 'Cornerstone's' interface to the statistical programming language 'R' has been available
    since version 6.0, the latest interface with 'R' is even much more efficient.
    'Cornerstone' release 7.1.1 allows you to integrate user defined 'R' packages directly into the
    standard 'Cornerstone' GUI.
    Your engineering team stays in 'Cornerstone's' graphical working environment and can apply 'R'
    routines, immediately and without the need to deal with programming code.
    Additionally, your 'R' programming team develops corresponding 'R' packages detached from
    'Cornerstone' in their favorite 'R' environment.

          Learn how to use 'R' packages in 'Cornerstone' 7.1.1 on 'camLineTV' YouTube channel 
    (<https://www.youtube.com/watch?v=HEQHwq_laXU>) (available in German).
	"""
	
	homepage = "https://gitlab.com/camLine/CornerstoneR/-/issues"
	cran = "CornerstoneR" 

	version("2.0.2", md5="88e362eaaaebec76fc2b4f94b7dec629")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-checkmate@1.9.1:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-spatialtools", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
