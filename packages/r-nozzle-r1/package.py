# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNozzleR1(RPackage):
	"""Nozzle Reports

	The Nozzle package provides an API to generate HTML
        reports with dynamic user interface elements based on
        JavaScript and CSS (Cascading Style Sheets). Nozzle was
        designed to facilitate summarization and rapid browsing of
        complex results in data analysis pipelines where multiple
        analyses are performed frequently on big data sets. The package
        can be applied to any project where user-friendly reports need
        to be created.
	"""
	
	homepage = "http://github.com/parklab/nozzle"
	cran = "Nozzle.R1" 

	version("1.1-1.1", md5="284892dbc261f1e919855a99e20b06ca", url="https://cran.r-project.org/src/contrib/Nozzle.R1_1.1-1.1.tar.gz")

