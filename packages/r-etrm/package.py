# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtrm(RPackage):
	"""Energy Trading and Risk Management

	Provides a collection of functions to perform core tasks within
    Energy Trading and Risk Management (ETRM). Calculation of maximum smoothness 
    forward price curves for electricity and natural gas contracts with flow delivery, as presented in
    F. E. Benth, S. Koekebakker, and F. Ollmar (2007) <doi:10.3905/jod.2007.694791>
    and F. E. Benth,  J. S. Benth,  and S. Koekebakker (2008) <doi:10.1142/6811>.
    Portfolio insurance trading strategies for price risk management in the forward market, see
    F. Black (1976) <doi:10.1016/0304-405X(76)90024-6>, 
    T. Bjork (2009) <https://EconPapers.repec.org/RePEc:oxp:obooks:9780199574742>,  
    F. Black and R. W. Jones (1987) <doi:10.3905/jpm.1987.409131> and
    H. E. Leland (1980) <http://www.jstor.org/stable/2327419>.
	"""
	
	cran = "etrm" 

	version("1.0.1", md5="37cd296d0f7cc8ab1eee4f117cddc9a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
