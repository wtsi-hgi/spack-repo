# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemochange(RPackage):
	"""Testing for Structural Breaks under Long Memory and Testing for
Changes in Persistence

	Test procedures and break point estimators for persistent processes that exhibit structural breaks in mean or in persistence.
    On the one hand the package contains the most popular approaches for testing whether a time series exhibits a break in persistence from I(0) to I(1) or vice versa, such as those of Busetti and Taylor (2004) and Leybourne, Kim, and Taylor (2007).
    The approach by Martins and Rodrigues (2014), which allows to detect changes from I(d1) to I(d2) with d1 and d2 being non-integers, is included as well.
    In case the tests reject the null of constant persistence, various breakpoint estimators are available to detect the point of the break as well as the order of integration in the two regimes.
    On the other hand the package contains the most popular approaches to test for a change-in-mean of a long-memory time series, which were recently reviewed by Wenger, Leschinski, and Sibbertsen (2018). 
    These include memory robust versions of the CUSUM, sup-Wald, and Wilcoxon type tests. The tests either utilize consistent estimates of the long-run variance or a self normalization approach in their test statistics.
    Betken (2016) <doi:10.1111/jtsa.12187>
    Busetti and Taylor (2004) <doi:10.1016/j.jeconom.2003.10.028>
    Dehling, Rooch and Taqqu (2012) <doi:10.1111/j.1467-9469.2012.00799.x>
    Harvey, Leybourne and Taylor (2006) <doi:10.1016/j.jeconom.2005.07.002>
    Horvath and Kokoszka (1997) <doi:10.1016/S0378-3758(96)00208-X>
    Hualde and Iacone (2017) <doi:10.1016/j.econlet.2016.10.014>
    Iacone, Leybourne and Taylor (2014) <doi:10.1111/jtsa.12049>
    Leybourne, Kim, Smith, and Newbold (2003) <doi:10.1111/1368-423X.t01-1-00110>
    Leybourne and Taylor (2004) <doi:10.1016/j.econlet.2003.12.015>
    Leybourne, Kim, and Taylor (2007): <doi:10.1111/j.1467-9892.2006.00517.x>
    Martins and Rodrigues (2014) <doi:10.1016/j.csda.2012.07.021>
    Shao (2011) <doi:10.1111/j.1467-9892.2010.00717.x>
    Sibbertsen and Kruse (2009) <doi:10.1111/j.1467-9892.2009.00611.x>
    Wang (2008) <doi:10.1080/00949650701216604>
    Wenger, Leschinski and Sibbertsen (2018) <doi:10.1016/j.econlet.2017.12.007>.
	"""
	
	cran = "memochange" 

	version("1.1.1", md5="a3109f82cb65a8ce045d1827a4487cd7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-urca@1.3:", type=("build", "run"))
	depends_on("r-forecast@8.6:", type=("build", "run"))
	depends_on("r-fracdiff@1.4.2:", type=("build", "run"))
	depends_on("r-longmemoryts@0.1:", type=("build", "run"))
	depends_on("r-sandwich@2.5.1:", type=("build", "run"))
	depends_on("r-strucchange@1.5.1:", type=("build", "run"))
	depends_on("r-longmemo@1.1.1:", type=("build", "run"))
