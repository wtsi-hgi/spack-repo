# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiureg(RPackage):
	"""Liu Regression with Liu Biasing Parameters and Statistics

	Linear Liu regression coefficient's estimation and testing with different Liu related measures such as MSE, R-squared etc.
  REFERENCES
  i.   Akdeniz and Kaciranlar (1995) <doi:10.1080/03610929508831585>
  ii.  Druilhet and Mom (2008) <doi:10.1016/j.jmva.2006.06.011>
  iii. Imdadullah, Aslam, and Saima (2017)
  iv.  Liu (1993) <doi:10.1080/03610929308831027>
  v.   Liu (2001) <doi:10.1016/j.jspi.2010.05.030>.
	"""
	
	cran = "liureg" 

	version("1.1.2", md5="f9e27858d97a0b0f58d67b7610de1dbe")

	depends_on("r@3.4:", type=("build", "run"))
