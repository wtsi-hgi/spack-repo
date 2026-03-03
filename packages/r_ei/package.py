# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REi(RPackage):
	"""Ecological Inference

	Software accompanying Gary King's book: A Solution to the Ecological Inference Problem. (1997). Princeton University Press. ISBN 978-0691012407. 
	"""
	
	homepage = "http://gking.harvard.edu/eiR"
	cran = "ei" 

	version("1.3-3", md5="3540ccdcadd160b355fb4579eaa15136")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-eipack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
