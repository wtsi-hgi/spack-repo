# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REchogram(RPackage):
	"""Echogram Visualisation and Analysis

	Easily import multi-frequency acoustic data stored in 'HAC' files (see <http://biblio.uqar.ca/archives/30005500.pdf> for more information on the format), and produce echogram visualisations with predefined or customized color palettes. It is also possible to merge consecutive echograms; mask or delete unwanted echogram areas; model and subtract background noise; and more important, develop, test and interpret different combinations of frequencies in order to perform acoustic filtering of the echogram's data. 
	"""
	
	homepage = "https://github.com/hvillalo/echogram"
	cran = "echogram" 

	version("0.1.2", md5="dd6edd3c9524d82fb7ea45982ab63035")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-readhac", type=("build", "run"))
