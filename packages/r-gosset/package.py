# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGosset(RPackage):
	"""Tools for Data Analysis in Experimental Agriculture

	Toolkit to analyse experimental agriculture data, 
    from data synthesis to model selection and visualisation. 
    The package is named after W.S. Gosset aka ‘Student’, a pioneer 
    of modern statistics in small sample experimental design and analysis.
	"""
	
	homepage = "https://agrdatasci.github.io/gosset/"
	cran = "gosset" 

	version("1.0", md5="b6e9217ccea63f458908c8e0438384d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bradleyterry2", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggparty", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-plackettluce", type=("build", "run"))
	depends_on("r-psychotools", type=("build", "run"))
	depends_on("r-qvcalc", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
