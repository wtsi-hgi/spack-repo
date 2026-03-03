# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProductivity(RPackage):
	"""Indices of Productivity Using Data Envelopment Analysis (DEA)

	
  Levels and changes of productivity and profitability are measured with various indices.
  The package contains the multiplicatively complete Färe-Primont, Fisher, Hicks-Moorsteen, 
  Laspeyres, Lowe, and Paasche indices, as well as the classic Malmquist productivity index.
  Färe-Primont and Lowe indices verify the transitivity property and can therefore be used for 
  multilateral or multitemporal comparison.
  Fisher, Hicks-Moorsteen, Laspeyres, Malmquist, and Paasche indices are not transitive and are 
  only to be used for binary comparison.
  All indices can also be decomposed into different components, providing insightful information 
  on the sources of productivity and profitability changes.
  In the use of Malmquist productivity index, the technological change index can be further 
  decomposed into bias technological change components.
  The package also allows to prohibit technological regression (negative technological change). In 
  the case of the Fisher, Hicks-Moorsteen, Laspeyres, Paasche and the transitive Färe-Primont 
  and Lowe indices, it is furthermore possible to rule out technological change. 
  Deflated shadow prices can also be obtained. Besides, the package allows parallel computing as 
  an option, depending on the user's computer configuration. 
  All computations are carried out with the nonparametric Data Envelopment Analysis (DEA), and 
  several assumptions regarding returns to scale are available.
  All DEA linear programs are implemented using 'lp_solve'.
	"""
	
	cran = "productivity" 

	version("1.1.0", md5="562a30418ea8ec679e1e81abdd748718")

	depends_on("r@2.15.3:", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
