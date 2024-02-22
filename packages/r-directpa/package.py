# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirectpa(RPackage):
	"""Direction Analysis for Pathways and Kinases

	Direction analysis is a set of tools designed to identify
    combinatorial effects of multiple treatments/conditions on pathways
    and kinases profiled by microarray, RNA-seq, proteomics, or phosphoproteomics
    data. See Yang P et al (2014) <doi:10.1093/bioinformatics/btt616>; and Yang P et al. (2016) <doi:10.1002/pmic.201600068>.
	"""
	
	cran = "directPA" 

	version("1.5.1", md5="fb97e41fc733cfdff3e40661804e649e")

	depends_on("r@3.10:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
