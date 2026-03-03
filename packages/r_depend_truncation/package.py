# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDependTruncation(RPackage):
	"""Statistical Methods for the Analysis of Dependently Truncated
Data

	Estimation and testing methods for dependently truncated data.
 Semi-parametric methods are based on Emura et al. (2011)<Stat Sinica 21:349-67>, Emura & Wang (2012)<doi:10.1016/j.jmva.2012.03.012>,
 and Emura & Murotani (2015)<doi:10.1007/s11749-015-0432-8>.
 Parametric approaches are based on Emura & Konno (2012)<doi:10.1007/s00362-014-0626-2> and Emura & Pan (2017)<doi:10.1007/s00362-017-0947-z>.
 A regression approach is based on Emura & Wang (2016)<doi:10.1007/s10463-015-0526-9>. Quasi-independence tests are based on Emura & Wang (2010)<doi:10.1016/j.jmva.2009.07.006>.
 Right-truncated data for Japanese male centenarians are given by Emura & Murotani (2015)<doi:10.1007/s11749-015-0432-8>.
	"""
	
	cran = "depend.truncation" 

	version("3.0", md5="aad9b85404594c6b9c09ccc07be9f697")

	depends_on("r-mvtnorm", type=("build", "run"))
