# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpetestnp(RPackage):
	"""Non-Parametric Tests of Parametric Specifications

	
    Performs non-parametric tests of parametric specifications.
    Five tests are available. 
    Specific bandwidth and kernel methods can be chosen along with many other options. 
    Allows parallel computing to quickly compute p-values based on the bootstrap. 
    Methods implemented in the package are H.J. Bierens (1982) <doi:10.1016/0304-4076(82)90105-1>,
    J.C. Escanciano (2006) <doi:10.1017/S0266466606060506>,
    P.L. Gozalo (1997) <doi:10.1016/S0304-4076(97)86571-2>,
    P. Lavergne and V. Patilea (2008) <doi:10.1016/j.jeconom.2007.08.014>,
    P. Lavergne and V. Patilea (2012) <doi:10.1198/jbes.2011.07152>,
    J.H. Stock and M.W. Watson (2006) <doi:10.1111/j.1538-4616.2007.00014.x>,
    C.F.J. Wu (1986) <doi:10.1214/aos/1176350142>,
    J. Yin, Z. Geng, R. Li, H. Wang (2010) <https://www.jstor.org/stable/24309002>
    and J.X. Zheng (1996) <doi:10.1016/0304-4076(95)01760-7>.
	"""
	
	homepage = "https://github.com/HippolyteBoucher/SpeTestNP"
	cran = "SpeTestNP" 

	version("1.1.0", md5="161c9219198a65e1c087bfd2a6b1873a")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
