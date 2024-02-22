# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegenvineq(RPackage):
	"""Environmental Inequality Indices Based on Segregation Measures

	A set of segregation-based indices and randomization methods to 
            make robust environmental inequality assessments, as described in 
            Schaeffer and Tivadar (2019) "Measuring Environmental Inequalities:
            Insights from the Residential Segregation Literature" 
            <doi:10.1016/j.ecolecon.2019.05.009>.
	"""
	
	cran = "SegEnvIneq" 

	version("1.1", md5="73019a00aa8870f25361094c85d46225")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-sf@1.0.14:", type=("build", "run"))
	depends_on("r-spdep@1.2.8:", type=("build", "run"))
	depends_on("r-oasisr@3.1:", type=("build", "run"))
	depends_on("r-outliers@0.15:", type=("build", "run"))
