# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRempsyc(RPackage):
	"""Convenience Functions for Psychology

	Make your workflow faster and easier. Easily customizable
    plots (via 'ggplot2'), nice APA tables (following the style of the
    *American Psychological Association*) exportable to Word (via
    'flextable'), easily run statistical tests or check assumptions, and
    automatize various other tasks.
	"""
	
	homepage = "https://rempsyc.remi-theriault.com"
	cran = "rempsyc" 

	version("0.1.7", md5="09ce1a160ab399c1c6bd62079b621497")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
