# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcssci(RPackage):
	"""Visualization of Restricted Cubic Splines

	Restricted Cubic Splines were performed to explore the shape of association form of "U, inverted U,
    L" shape and test linearity or non-linearity base on "Cox,Logistic,linear,quasipoisson" regression, and auto output Restricted Cubic Splines figures.
    rcssci package could automatically draw RCS graphics with Y-axis "OR,HR,RR,beta".
    The Restricted Cubic Splines method were based on 
    Suli Huang (2022) <doi:10.1016/j.ecoenv.2022.113183>,Amit Kaura (2019) <doi:10.1136/bmj.l6055>,
    and Harrell Jr (2015, ISBN:978-3-319-19424-0 (Print) 978-3-319-19425-7 (Online)).
	"""
	
	cran = "rcssci" 

	version("0.4.0", md5="727dc6909a6f7e6bb75cf6902dea3152")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-pacman", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
