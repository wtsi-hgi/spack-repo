# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REducineq(RPackage):
	"""Compute and Decompose Inequality in Education

	Easily compute education inequality measures and the distribution 
  of educational attainments for any group of countries, using the data set 
  developed in Jorda, V. and Alonso, JM. (2017) <DOI:10.1016/j.worlddev.2016.10.005>. 
  The package offers the possibility to compute not only the Gini index, but 
  also generalized entropy measures for different values of the sensitivity 
  parameter. In particular, the package includes functions to compute the 
  mean log deviation, which is more sensitive to the bottom part of the 
  distribution; the Theil’s entropy measure, equally sensitive to all parts 
  of the distribution; and finally, the GE measure when the sensitivity 
  parameter is set equal to 2, which gives more weight to differences in 
  higher education. The decomposition of these measures in the components 
  between-country and within-country inequality is also provided. Two 
  graphical tools are also provided, to analyse the evolution of the
  distribution of educational attainments: The cumulative distribution 
  function and the Lorenz curve.
	"""
	
	cran = "educineq" 

	version("0.1.0", md5="2232d5bfb38b9d538386d9655a2ceb77")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
